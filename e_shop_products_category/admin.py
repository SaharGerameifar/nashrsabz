from django.contrib import admin

from .models import ProductCategory


# Register your models here.


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__']

    class Meta:
        model = ProductCategory


admin.site.register(ProductCategory, ProductCategoryAdmin)