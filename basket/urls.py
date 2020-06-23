from django.urls import path
from .views import show_basket, add_to_basket

urlpatterns = [
    path('', show_basket, name='basket'),
    path('add_item/<item_id>', add_to_basket, name='add-to-basket'),
]