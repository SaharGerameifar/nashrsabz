# Generated by Django 3.2.8 on 2005-12-31 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop_settings', '0003_sitesettings_location_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='return_us',
            field=models.TextField(blank=True, null=True, verbose_name='رویه بازگشت کالا'),
        ),
    ]
