from django.db import models
import os


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.title}{ext}"
    return f"setting-image/{final_name}"


class SiteSettings(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان سایت')
    address = models.CharField(max_length=250, verbose_name='آدرس')
    phone = models.CharField(max_length=50, verbose_name='تلفن')
    mobile = models.CharField(max_length=50, verbose_name='تلفن همراه')
    fax = models.CharField(max_length=50, verbose_name='فکس')
    email = models.EmailField(max_length=50, verbose_name='ایمیل')
    about_us = models.TextField(verbose_name='درباره ما', null=True, blank=True)
    copy_right = models.TextField(verbose_name='متن کپی رایت', null=True, blank=True)
    logo_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر لوگو')
    location_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر لوکیشن ما')
    instagram = models.CharField(max_length=150, verbose_name=' آدرس اینستاگرام', null=True, blank=True)
    linkedin = models.CharField(max_length=150, verbose_name=' آدرس تلگرام', null=True, blank=True)

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'مدیریت تنظیمات'

    def __str__(self):
        return self.title


class ReturnSettings(models.Model):
    question = models.TextField(verbose_name='سوال', null=True, blank=True)
    answer = models.TextField(verbose_name='پاسخ', null=True, blank=True)

    class Meta:
        verbose_name = 'رویه بازگشت کالا '
        verbose_name_plural = 'رویه بازگشت کالا'

    def __str__(self):
        return self.question


class FAQSettings(models.Model):
    question = models.TextField(verbose_name='سوال', null=True, blank=True)
    answer = models.TextField(verbose_name='پاسخ', null=True, blank=True)

    class Meta:
        verbose_name = 'سوالات متداول '
        verbose_name_plural = 'سوالات متداول '

    def __str__(self):
        return self.question


class LawSettings(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان', null=True, blank=True)
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)

    class Meta:
        verbose_name = 'قوانین و مقررات سایت'
        verbose_name_plural = 'قوانین و مقررات سایت '

    def __str__(self):
        return self.title
