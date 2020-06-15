from django.urls import path
from .views import show_products, show_product_detail, show_category_products

urlpatterns = [
    path('', show_products, name='products-home'),
    path('product-detail/<int:id>', show_product_detail, name='product-detail'),
    path('category-products/<int:id>', show_category_products, name='category-products'),
]