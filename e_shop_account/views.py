from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from e_shop_products.models import Product
from utilities.EmailService import EmailService
from .forms import (LoginForm, RegisterForm, EditUserForm, EditProfileForm, ChangePasswordForm)
from django.contrib.auth import login, get_user_model, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            login_form.add_error('user_name', 'کاربری با مشخصات وارد شده یافت نشد')

    context = {
        'login_form': login_form,
        'title': 'ورود',
    }
    return render(request, 'account/login.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('user_name')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')
        # EmailService.send_email(
        #     'ايميل فعال سازي نشر سبز',
        #     [email],
        #     'Emails/test_email.html',
        #     {
        #         'title': 'ايميل فعال سازي نشر سبز',
        #         'description': 'براي فعال ساري سازي اكانت خود روي لينك زير كليك كنيد.'
        #     })

        User.objects.create_user(username=user_name, email=email, password=password, is_staff=False)
        user_id = User.objects.filter(username=user_name).first().id
        Profile.objects.create(user_id=user_id)

        return redirect('/register-done')

    context = {
        'register_form': register_form,
        'title': 'ثبت نام',
    }
    return render(request, 'account/register.html', context)


def register_done(request):
    return render(request, 'account/register-done.html', {'title': 'ثبت نام موفقيت آميز  شما '})


def log_out(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='/login')
def user_account_main_page(request):
    profile = request.user.profile
    context = {
        'profile': profile,
        'title': 'اطلاعات كاربري',
    }
    return render(request, 'account/user_account_main.html', context)


def user_sidebar(request):
    context = {
    }
    return render(request, 'account/user_sidebar.html', context)


@login_required(login_url='/login')
def edit_user_account(request):
    if request.method == 'POST':
        edit_profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile )
        edit_user_form = EditUserForm(request.POST, instance=request.user)
        if edit_profile_form.is_valid() and edit_user_form.is_valid():
            edit_profile_form.save()
            edit_user_form.save()
            # return HttpResponseRedirect('/user')
    else:
        edit_profile_form = EditProfileForm(instance=request.user.profile)
        edit_user_form = EditUserForm(instance=request.user)
    context = {
        'edit_profile_form': edit_profile_form,
        'profile_image': request.user.profile.profile_image,
        'edit_form': edit_user_form,
        'title': 'اطلاعات كاربري',
    }
    return render(request, 'account/edit_user_account.html', context)


@login_required(login_url='/login')
def chang_user_password(request):
    if request.method == 'POST':
        change_password_form = ChangePasswordForm(request.POST)
        if change_password_form.is_valid():
            new_password = change_password_form.cleaned_data.get('password')
            request.user.set_password(new_password)
            request.user.save()
            return HttpResponseRedirect('/user')
    else:
        change_password_form = ChangePasswordForm()
    context = {
        'title': 'تغيير كلمه عبور',
        'change_password_form': change_password_form,
    }
    return render(request, 'account/change_user_password.html', context)


@login_required(login_url='/login')
def user_likes(request):
    context = {
        'likes': None,
        'title': ' علاقه مندي ها',
    }
    user = request.user
    products_liked = Product.objects.get_active_product().filter(likes=user)
    if products_liked is not None:
        context['likes'] = products_liked

    return render(request, 'account/user_likes.html', context)
