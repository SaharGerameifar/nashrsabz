from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from e_shop_products.models import Product


class Tag(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='عنوان در url')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    active = models.BooleanField(verbose_name='فعال/غیر فعال', default=False)
    products = models.ManyToManyField(Product, blank=True, verbose_name='محصولات')

    class Meta:
        verbose_name_plural = 'برچسب ها/ تگ ها'
        verbose_name = 'برچسب / تگ'

    def __str__(self):
        return self.title


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_receiver, sender=Tag)
