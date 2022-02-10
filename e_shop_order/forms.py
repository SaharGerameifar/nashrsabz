from django import forms
from .models import Order
from django.contrib.auth.models import User
from django.core import validators


class UserNewOrder(forms.Form):
    product_id = forms.IntegerField(
        widget=forms.HiddenInput(),
    )
    count = forms.IntegerField(
        widget=forms.NumberInput(),
        initial=1,
        label='تعداد',
    )


class OrderCheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'family', 'mobile', 'address', 'postcode', 'provance', 'city')
        labels = {
            'name': 'نام',
            'family': 'نام خانوادگی',
            'mobile': 'موبایل',
            'address': 'آدرس',
            'postcode': 'كد پستي',
            'provance': 'استان',
            'city': 'شهر',
        }




