from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room


@login_required
def chat(request):
	rooms = Room.objects.all()

	return render(request, 'chat/chat.html', {'rooms': rooms})


@login_required
def room(request, id):
	room = Room.objects.get(pk=id)

	return render(request, 'chat/room.html', {'room': room})
