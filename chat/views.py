from django.shortcuts import render


def chat(request):
	"""Renders a page with choices for chat rooms"""

	return render(request, 'chat/chat.html')
