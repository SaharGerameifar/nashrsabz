import time
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from e_shop_order.forms import UserNewOrder, OrderCheckoutForm
from e_shop_order.models import (Order, OrderDetail)
from e_shop_products.models import Product
from zeep import Client
from decouple import config

# Create your views here.


@login_required(login_url='/login')
def add_user_order(request):
    new_order_form = UserNewOrder(request.POST or None)
    if new_order_form.is_valid():
        order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id, is_paid=False)
        product_id = new_order_form.cleaned_data.get('product_id')
        count = new_order_form.cleaned_data.get('count')
        if count < 0:
            count = 1
        product = Product.objects.get_by_id(product_id=product_id)

        exist_product = OrderDetail.objects.filter(product_id=product_id, order_id=order.id).first()
        if exist_product is None:
            order.orderdetail_set.create(product_id=product_id, price=product.price, count=count)
        else:
            count = exist_product.count + count
            OrderDetail.delete(exist_product)
            order.orderdetail_set.create(product_id=product_id, price=product.price, count=count)
        return redirect(f'/products/{product.id}/{product.title.replace(" ", "-")}')
    return redirect('/')


@login_required(login_url='/login')
def user_open_order(request):
    context = {
        'order': None,
        'details': None,
        'total': 0,
        'title': 'سبد خرید'
    }
    open_order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if open_order is not None:
        context['order'] = open_order
        context['details'] = open_order.orderdetail_set.all()
        context['total'] = open_order.get_total_price()

    return render(request, 'order/user_open_order.html', context)


@login_required(login_url='/login')
def check_out(request):

    order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()

    if request.method == 'POST':
        form = OrderCheckoutForm(request.POST)
        if form.is_valid():
            if order is not None:
                name = form.cleaned_data.get('name')
                family = form.cleaned_data.get('family')
                mobile = form.cleaned_data.get('mobile')
                postcode = form.cleaned_data.get('postcode')
                provance = form.cleaned_data.get('provance')
                city = form.cleaned_data.get('city')
                address = form.cleaned_data.get('address')
                order.name = name
                order.family = family
                order.mobile = mobile
                order.postcode = postcode
                order.provance = provance
                order.city = city
                order.address = address
                order.save()
                return redirect('/payment')
    else:
        form = OrderCheckoutForm()

    context = {
        'title': 'افزودن آدرس',
        'form': form,
        'total': order.get_total_price(),
    }

    return render(request, 'order/user_check_out.html', context)


@login_required(login_url='/login')
def remove_order_detail(request, *args, **kwargs):
    detail_id = kwargs.get('detail_id')
    if detail_id is not None:
        order_detail = OrderDetail.objects.get_queryset().get(id=detail_id, order__owner_id=request.user.id)
        if order_detail is not None:
            order_detail.delete()
            return redirect('/open_order')
    raise Http404


@login_required(login_url='/login')
def paid_order(request):

    paid_order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=True)
    context = {
        'title': 'ليست سفارشات من',
        'order': None,
    }
    if paid_order is not None:
        context['order'] = paid_order


    return render(request, 'order/user_paid_order.html', context)


@login_required(login_url='/login')
def detail_paid_order(request, *args, **kwargs):
    context = {
        'title': 'جزئيات سفارش من',
        'details': None,
    }
    order_id = kwargs.get('order_id')
    if order_id is not None:
        order_detail = OrderDetail.objects.filter(order=order_id, order__owner_id=request.user.id)
        context['details'] = order_detail
    return render(request, 'order/detail_paid_order.html', context)



# MERCHANT = config('MERCHANT')
amount = 500  # Toman / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '00'  # Optional

# client = config('client')
# CallbackURL = config('CallbackURL')


def send_request(request, *args, **kwargs):
    total_price = 0
    open_order: Order = Order.objects.filter(is_paid=False, owner_id=request.user.id).first()
    if open_order is not None:
        total_price = open_order.get_total_price()
        mobile = open_order.mobile
        email = open_order.owner.email
        description = "تراكنش شما در نشر سبز"
        result = client.service.PaymentRequest(
            MERCHANT, total_price, description, email, mobile, f"{CallbackURL}/{open_order.id}"
        )
        if result.Status == 100:
            return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
        else:
            return HttpResponse('Error code: ' + str(result.Status))
    raise Http404()


def verify(request, *args, **kwargs):
    order_id = kwargs.get('order_id')
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            user_order = Order.objects.get_queryset().get(id=order_id)
            user_order.is_paid = True
            user_order.payment_date = time.time()
            user_order.ref_id = result.RefID
            user_order.save()
            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')

