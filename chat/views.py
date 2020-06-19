from django.shortcuts import render


def chat(request):
	"""
	Renders a page with a message containing a link 
	to the chat feature
	"""

	return render(request, 'chat/chat.html')
