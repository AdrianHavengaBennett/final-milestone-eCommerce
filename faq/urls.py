from django.urls import path

from .views import show_faqs

urlpatterns = [
    path('', show_faqs, name='faqs-home'),
]
