# Generated by Django 3.2.8 on 2005-12-31 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop_order', '0006_alter_order_postcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='mobile',
            field=models.IntegerField(blank=True, max_length=11, verbose_name='شماره تماس مشتري'),
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='كد پستي مشتري'),
        ),
    ]
