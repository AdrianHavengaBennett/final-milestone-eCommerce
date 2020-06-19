from django.shortcuts import render
from django.db.models import Q
from blog.models import BlogPost
from products.models import Product
from faq.models import FAQ
from shows.models import UpcomingShows
from products.views import do_pagination


def blog_search(request):
	"""
	Does a search on all blog posts and sends a searched value
	to the template in order to ascertain whether or not the query set
	has been filtered and also leaves a reminder of what was searched
	"""

	context = do_pagination(request, products=BlogPost.objects.filter(title__icontains=request.GET['b-search']))

	context['searched_str'] = request.GET['b-search']

	return render(request, 'blog/blog_home.html', context)


def products_search(request):
	"""
	Does a search on all products and sends a searched value
	to the template in order to ascertain whether or not the query set
	has been filtered and also leaves a reminder of what was searched
	"""

	context = do_pagination(request, products=Product.objects.filter(name__icontains=request.GET['p-search']))

	context['searched_str'] = request.GET['p-search']

	return render(request, 'products/index.html', context)


def faqs_search(request):
	"""
	Does a search on all faqs and sends a searched value
	to the template in order to ascertain whether or not the query set
	has been filtered and also leaves a reminder of what was searched
	"""

	faqs = FAQ.objects.filter(question__icontains=request.GET['f-search'])
	searched_str = request.GET['f-search']

	context = {
		'faqs': faqs,
		'searched_str': searched_str
	}

	return render(request, 'faq/faq.html', context)


def shows_search(request):
	"""
	Does a search on all shows and sends a searched value
	to the template in order to ascertain whether or not the query set
	has been filtered and also leaves a reminder of what was searched
	"""

	searched_str = request.GET['s-search']

	shows = UpcomingShows.objects.filter(
		Q(artist_name__icontains=searched_str)|
		Q(venue__location_name__icontains=searched_str)
	)

	context = {
		'shows': shows,
		'searched_str': searched_str
	}

	return render(request, 'shows/shows.html', context)
