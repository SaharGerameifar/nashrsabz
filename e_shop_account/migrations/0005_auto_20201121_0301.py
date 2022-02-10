# Generated by Django 3.2.8 on 2020-11-20 23:31

from django.db import migrations, models
import e_shop_account.models


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop_account', '0004_auto_20201121_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(1, 'زن'), (2, 'مرد')], null=True, verbose_name='جنسیت'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=e_shop_account.models.upload_image_path, verbose_name='تصویر'),
        ),
    ]
