from django.urls import path
from .views import get_help

urlpatterns = [
    path('', get_help, name='help'),
]