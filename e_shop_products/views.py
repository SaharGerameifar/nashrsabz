from django.shortcuts import render, redirect
from django.views.generic import ListView
from e_shop_order.forms import UserNewOrder
from .models import (Product, ProductGalley)
from django.http import Http404
from e_shop_tag.models import Tag
from e_shop_products_category.models import ProductCategory
from django.contrib.auth.decorators import login_required
import itertools


class ProductsList(ListView):
    template_name = 'products/product_list.html'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.get_active_product()


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def product_detail(request, *args, **kwargs):
    selected_product_id = kwargs['productId']
    new_order_form = UserNewOrder(request.POST or None, initial={'product_id': selected_product_id})
    product = Product.objects.get_by_id(selected_product_id)
    if product is None:
        raise Http404("محصول مورد نظر یافت نشد")
    product.visit_count += 1
    product.save()
    galleries = ProductGalley.objects.filter(product_id=selected_product_id)
    grouped_galleries = my_grouper(3, galleries)
    related_products = Product.objects.get_active_product().filter(categories__product=product).distinct()
    grouped_related_products = my_grouper(3, related_products)
    context = {
        'product': product,
        'product_tag_list': product.tag_set.all(),
        'galleries': grouped_galleries,
        'related_products': grouped_related_products,
        'new_order_form': new_order_form,
        'title': product.title ,
    }
    # print(product.tag_set.all())
    return render(request, 'products/product_detail.html', context)


class SearchProductsView(ListView):
    template_name = 'products/product_list.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        query = request.GET.get('query')
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.get_active_product()


class ProductsListByCategory(ListView):
    template_name = 'products/product_list.html'
    paginate_by = 6

    def get_queryset(self):
        category_name = self.kwargs['title'].replace('-', ' ')
        category = ProductCategory.objects.filter(title__iexact=category_name).first()
        if category is None:
            raise Http404('صفحه ی مورد نظر یافت نشد')
        return Product.objects.get_by_category(category_name)


def product_categories_partial(request):
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'products/products_categories_partial.html', context)


@login_required(login_url='/login')
def product_like(request, *args, **kwargs):
    selected_product_id = kwargs['productId']
    product = Product.objects.get_by_id(selected_product_id)
    user = request.user
    if user not in product.likes.all():
        product.likes.add(user)
        return redirect(f'/products/{product.id}/{product.title.replace(" ", "-")}')
    product.likes.remove(user)
    return redirect(f'/products/{product.id}/{product.title.replace(" ", "-")}')

