from django.shortcuts import render
from .models import FAQ

def show_faqs(request):
	"""Renders all of the current frequently asked questions
	to the faq.html page
	"""

	faqs = FAQ.objects.all()

	return render(request, 'faq/faq.html', {'faqs': faqs})
