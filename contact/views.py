from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import ContactForm
from click_and_collect.models import ClickCollectLocations

OUR_OFFICE = ClickCollectLocations.objects.filter(location_name__contains='Our Office').first()


def contact_us(request):
	"""
	Renders a contact form to the contact.html page and
	also the contact info of the business for the Google Map
	"""

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			return redirect('thank-you')
	else:
		form = ContactForm()

	context = {
		'form': form,
		'our_office': OUR_OFFICE
	}

	return render(request, 'contact/contact.html', context)


def thank_you(request):
	"""
	Renders a thank you message and the business info to
	the thank_you.html page
	"""

	return render(request, 'contact/thank_you.html', {'our_office': OUR_OFFICE})
