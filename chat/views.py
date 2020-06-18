from django.shortcuts import render


def get_help(request):
	"""
	Renders a page with a message containing a link 
	to the help chatbot API
	"""

	return render(request, 'help/help.html')
