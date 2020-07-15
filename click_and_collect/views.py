from django.shortcuts import render
from .models import ClickCollectLocations


def get_location(request, keywords):

	location = ClickCollectLocations.objects.get(location_name__icontains=keywords)

	return location


def click_and_collect(request):
	"""Renders the click&collect dropoff locations and makes
	use of the Google Maps API
	"""

	locations = ClickCollectLocations.objects.all().exclude(
		location_name__exact='Our Office'
	).exclude(
		location_name__exact='Fusion Club'
	).exclude(
		location_name__exact='The Bar'
	)

	return render(request, 'click_and_collect/click_and_collect_locations.html',
		{'locations': locations})
