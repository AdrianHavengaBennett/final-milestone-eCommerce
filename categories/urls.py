from django.urls import path

from .views import show_categories

urlpatterns = [
    path('', show_categories, name='categories'),
]
