# Generated by Django 3.2.8 on 2005-12-31 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop_products_category', '0001_initial'),
        ('e_shop_products', '0002_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, to='e_shop_products_category.ProductCategory', verbose_name='دسته بندی ها'),
        ),
    ]
