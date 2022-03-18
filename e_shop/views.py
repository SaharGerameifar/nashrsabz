import itertools
from django.shortcuts import render, redirect
from e_shop_products_category.models import ProductCategory
from e_shop_slider.models import Slider
from e_shop_settings.models import SiteSettings, ReturnSettings, FAQSettings, LawSettings
from e_shop_products.models import Product
from utilities.EmailService import EmailService


def header(request, *args, **kwargs):
    site_settings = SiteSettings.objects.first()
    categories = ProductCategory.objects.all()
    context = {
        'settings': site_settings,
        'categories': categories,
    }

    return render(request, 'shared/Header.html', context)


# footer code behind
def footer(request, *args, **kwargs):
    site_settings = SiteSettings.objects.first()
    context = {
        'settings': site_settings,
    }
    return render(request, 'shared/Footer.html', context)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


# code behind
def home_page(request):
    sliders = Slider.objects.all()
    most_visited_product = Product.objects.order_by('-visit_count').all()[:8]
    latest_product = Product.objects.order_by('-id').all()[:8]

    context = {
        'sliders': sliders,
        'title': 'صفحه اصلی ',
        'most_visited_products': my_grouper(4, most_visited_product),
        'latest_products': my_grouper(4, latest_product),

    }

    return render(request, 'home_page.html', context)


def about_page(request):
    site_settings = SiteSettings.objects.first()
    context = {
        'settings': site_settings,
        'title': 'درباره ما',
    }
    return render(request, 'about_page.html', context)


def handle_404_error(request, exception):
    site_settings = SiteSettings.objects.first()
    context = {
        'settings': site_settings,
    }
    return render(request, '404.html', context)


def return_us_page(request):
    question = ReturnSettings.objects.all()
    context = {
        'questions': question,
        'title': 'رويه بازگشت كالا',
    }
    return render(request, 'return_us_page.html', context)


def faq_page(request):
    faqs = FAQSettings.objects.all()
    context = {
        'faqs': faqs,
        'title': 'سوالات متداول',
    }
    return render(request, 'faq_page.html', context)


def law_page(request):
    laws = LawSettings.objects.all()
    site_settings = SiteSettings.objects.first()
    context = {
        'laws': laws,
        'settings': site_settings,
        'title': 'قوانين و مقررات سايت ',
    }
    return render(request, 'law_page.html', context)
