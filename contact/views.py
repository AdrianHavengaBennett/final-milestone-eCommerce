from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import ContactForm
from click_and_collect.models import ClickCollectLocations


def get_office_location(request):
	"""Helper function retrieves office location"""

	our_office = ClickCollectLocations.objects.filter(location_name__contains='Our Office').first()

	return our_office


def contact_us(request):
	"""Renders a contact form to the contact.html page and
	also the contact info of the business for the Google Map
	"""

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			return redirect('thank-you')
	else:
		form = ContactForm()

	our_office = get_office_location(request)

	context = {
		'form': form,
		'our_office': our_office
	}

	return render(request, 'contact/contact.html', context)


def thank_you(request):
	"""Renders a thank you message and the business info to
	the thank_you.html page
	"""

	our_office = get_office_location(request)

	return render(request, 'contact/thank_you.html', {'our_office': our_office})
