from django.urls import path

from .views import register, logout_user, profile, order_history

urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path('order_history/<order_number>', order_history, name='order-history'),
]
