from django.urls import path
from .views import register, logout_user, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
]