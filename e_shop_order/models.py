from django.contrib.auth.models import User
from django.db import models
from e_shop_products.models import Product
from extensions.utils import jalali_converter


# Create your models here.


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(verbose_name='پرداخت شده / نشده')
    payment_date = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')
    ref_id = models.BigIntegerField(blank=True, null=True, verbose_name='کد پیگیری سبد پرداخت شده')
    name = models.CharField(max_length=200, verbose_name="نام مشتري", blank=True, null=True,)
    family = models.CharField(max_length=200, verbose_name="نام خانوادگي مشتري", blank=True, null=True,)
    postcode = models.CharField(max_length=200, null=True, blank=True, verbose_name="كد پستي مشتري")
    mobile = models.IntegerField( verbose_name="شماره تماس مشتري", blank=True, null=True,)
    address = models.TextField(max_length=500, blank=True, verbose_name="آدرس مشتري")
    provance = models.CharField(max_length=500, blank=True, verbose_name="استان", null=True,)
    city = models.CharField(max_length=500, blank=True, verbose_name="شهر", null=True,)

    def get_total_price(self):
        amount = 0
        for detail in self.orderdetail_set.all():
            amount += detail.price * detail.count
        return amount

    def jpayment_date(self):
        return jalali_converter(self.payment_date)
    jpayment_date.short_description = 'تاریخ پرداخت'

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید کاربران'

    def __str__(self):
        return self.owner.username


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    price = models.IntegerField(verbose_name='قیمت محصول')
    count = models.IntegerField(verbose_name='تعداد')

    def get_detail_sum(self):
        return self.count * self.price

    class Meta:
        verbose_name = 'جزئیات محصول'
        verbose_name_plural = 'اطلاعات جزئیات محصولات'

    def __str__(self):
        return self.product.title


