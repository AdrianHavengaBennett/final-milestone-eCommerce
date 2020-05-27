from django.urls import path
from .views import show_all_posts

urlpatterns = [
    path('', show_all_posts, name='blog-home'),
]