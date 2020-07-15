from django.urls import path
from .views import click_and_collect, get_location

urlpatterns = [
    path('', click_and_collect, name='click_and_collect'),
    path('get-location/<keywords>/', get_location, name='get-location'),
]
