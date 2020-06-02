from django.urls import path
from .views import show_products, show_product_detail

urlpatterns = [
    path('', show_products, name='products-home'),
    path('product_detail/<int:id>', show_product_detail, name='product-detail'),
]