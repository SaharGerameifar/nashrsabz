# Generated by Django 3.2.8 on 2020-11-26 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop_settings', '0008_returnsettings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='returnsettings',
            name='image',
        ),
    ]
