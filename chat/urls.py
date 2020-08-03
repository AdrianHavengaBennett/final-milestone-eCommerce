from django.urls import path

from .views import chat, room

urlpatterns = [
    path('', chat, name='chat'),
    path('<int:id>/', room, name='room'),
]
