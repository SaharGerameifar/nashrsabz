from django.contrib.auth.models import User
from django.db import models
import os


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.user.username}{ext}"
    return f"profile/{final_name}"


class Profile(models.Model):
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = ' کاربران'

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='نام کاربری', related_name='profile')
    profile_image = models.ImageField(upload_to=upload_image_path, verbose_name='تصویر', null=True, blank=True)
    woman = 1
    man = 2
    status_choice = ((woman, 'زن'), (man, 'مرد'))
    gender = models.IntegerField(choices=status_choice, verbose_name='جنسیت', null=True, blank=True)

    def __str__(self):
        return self.user.username
