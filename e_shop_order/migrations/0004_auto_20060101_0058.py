# Generated by Django 3.2.8 on 2005-12-31 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop_order', '0003_alter_order_ref_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(blank=True, default='111', max_length=500, verbose_name='آدرس مشتري'),
        ),
        migrations.AddField(
            model_name='order',
            name='family',
            field=models.CharField(default='111', max_length=200, verbose_name='نام خانوادگي مشتري'),
        ),
        migrations.AddField(
            model_name='order',
            name='mobile',
            field=models.CharField(default='111', max_length=11, verbose_name='شماره تماس مشتري'),
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default='111', max_length=200, verbose_name='نام مشتري'),
        ),
        migrations.AddField(
            model_name='order',
            name='postcode',
            field=models.EmailField(default='111', max_length=200, null=True, verbose_name='كد پستي مشتري'),
        ),
    ]
