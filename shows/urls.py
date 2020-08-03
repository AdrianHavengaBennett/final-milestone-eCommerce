from django.urls import path

from .views import get_shows, show_details

urlpatterns = [
    path('', get_shows, name='get-shows'),
    path('show-details/<int:id>', show_details, name='show-details'),
]
