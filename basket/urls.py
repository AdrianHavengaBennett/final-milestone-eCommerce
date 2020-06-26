from django.urls import path
from .views import show_basket, add_to_basket, update_basket, remove_from_basket

urlpatterns = [
    path('', show_basket, name='basket'),
    path('add_item/<item_id>/', add_to_basket, name='add-to-basket'),
    path('update/<item_id>/', update_basket, name='update-basket'),
    path('remove/<item_id>/', remove_from_basket, name='remove-item'),
]