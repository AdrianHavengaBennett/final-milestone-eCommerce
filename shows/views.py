from django.shortcuts import render
from .models import UpcomingShows, ShowsTickets
from click_and_collect.models import ClickCollectLocations


def get_shows(request):
	"""Renders all current shows to the shows.html page"""

	shows = UpcomingShows.objects.all()

	return render(request, 'shows/shows.html', {'shows': shows})


def show_details(request, id):
	"""
	Retrieves the show by id and renders the details
	to the show_detail.html page
	"""

	show = UpcomingShows.objects.get(pk=id)
	the_bar = ClickCollectLocations.objects.get(location_name__exact='The Bar')
	fusion_club = ClickCollectLocations.objects.get(location_name__exact='Fusion Club')

	tickets = ShowsTickets.objects.get(artist_id=show.id)

	context = {
		'show': show,
		'the_bar': the_bar,
		'fusion_club': fusion_club,
		'tickets': tickets
	}

	return render(request, 'shows/show_details.html', context)

