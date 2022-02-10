# Generated by Django 3.2.8 on 2021-10-29 22:56

from django.db import migrations, models
import e_shop_products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('image', models.ImageField(blank=True, null=True, upload_to=e_shop_products.models.upload_image_path, verbose_name='تصویر')),
                ('active', models.BooleanField(default=False, verbose_name='فعال/غیر فعال')),
            ],
        ),
    ]
