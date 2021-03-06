# Generated by Django 3.2.8 on 2020-11-20 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import e_shop_account.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='نام')),
                ('family', models.CharField(max_length=150, verbose_name='نام خانوادگی')),
                ('profile_image', models.ImageField(upload_to=e_shop_account.models.upload_image_path, verbose_name='تصویر')),
                ('gender', models.IntegerField(choices=[(1, 'زن'), (2, 'مرد')], verbose_name='جنسیت')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربری')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': ' کاربران',
            },
        ),
    ]
