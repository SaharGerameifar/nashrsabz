# Generated by Django 3.2.8 on 2021-11-22 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop_products_category', '0002_auto_20211122_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='slug',
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='title',
            field=models.CharField(max_length=150, verbose_name='عنوان'),
        ),
    ]
