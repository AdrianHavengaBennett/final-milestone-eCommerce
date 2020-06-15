from django.urls import path
from .views import (
	blog_search,
	products_search,
	faqs_search,
	shows_search
)

urlpatterns = [
    path('', blog_search, name='blog-search'),
    path('products-search/', products_search, name='products-search'),
    path('faqs-search/', faqs_search, name='faqs-search'),
    path('shows-search/', shows_search, name='shows-search'),
]
