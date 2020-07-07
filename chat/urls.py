from django.urls import path
from .views import chat, room

from django.urls import path
from . import views

urlpatterns = [
    path('', chat, name='chat'),
    path('<int:id>/', room, name='room'),
]
