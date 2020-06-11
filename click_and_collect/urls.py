from django.urls import path
from .views import click_and_collect

urlpatterns = [
    path('', click_and_collect, name='click_and_collect'),
]
