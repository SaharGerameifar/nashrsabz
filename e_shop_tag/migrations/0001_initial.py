# Generated by Django 3.2.8 on 2019-10-30 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('e_shop_products', '0002_alter_product_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='عنوان')),
                ('slug', models.SlugField(verbose_name='عنوان در url')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('active', models.BooleanField(default=False, verbose_name='فعال/غیر فعال')),
                ('products', models.ManyToManyField(blank=True, to='e_shop_products.Product', verbose_name='محصولات')),
            ],
            options={
                'verbose_name': 'برچسب / تگ',
                'verbose_name_plural': 'برچسب ها/ تگ ها',
            },
        ),
    ]
