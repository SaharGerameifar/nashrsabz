from django.urls import path
from .views import (ProductsList, product_detail, SearchProductsView, ProductsListByCategory, product_categories_partial, product_like)


urlpatterns = [
    path('products', ProductsList.as_view()),
    path('products/<productId>/<title>', product_detail),
    path('products_like/<productId>', product_like),
    path('products/search', SearchProductsView.as_view()),
    path('products/<title>', ProductsListByCategory.as_view()),
    path('product_categories_partial', product_categories_partial, name='product_categories_partial'),
]
