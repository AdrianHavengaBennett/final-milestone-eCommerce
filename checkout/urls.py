from django.urls import path

from .views import checkout, checkout_success, get_location_info

urlpatterns = [
    path('', checkout, name='checkout'),
    path('checkout_success/<order_number>',
         checkout_success, name='checkout-success'),
    path('ajax/get_location_info',
         get_location_info, name='get-location-info'),
]
