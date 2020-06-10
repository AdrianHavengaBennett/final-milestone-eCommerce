from django.shortcuts import render
from blog.models import BlogPost
from products.models import Product
from faq.models import FAQ


def blog_search(request):
	"""
	Does a search on the blog posts and sends a Boolean value
	to the template in order to ascertain whether or not the query set
	has been filtered
	"""

	blog_posts = BlogPost.objects.filter(title__icontains=request.GET['b-search'])
	searched_str = request.GET['b-search']

	context = {
		'posts': blog_posts,
		'searched_str': searched_str
	}

	return render(request, 'blog/blog_home.html', context)


def products_search(request):
	"""
	Does a search on all products and sends a Boolean value
	to the template in order to ascertain whether or not the query set
	has been filtered
	"""

	products = Product.objects.filter(name__icontains=request.GET['p-search'])
	searched_str = request.GET['p-search']

	context = {
		'products': products,
		'searched_str': searched_str
	}

	return render(request, 'products/index.html', context)


def faqs_search(request):
	"""
	Does a search on all faqs and sends a Boolean value
	to the template in order to ascertain whether or not the query set
	has been filtered
	"""

	faqs = FAQ.objects.filter(question__icontains=request.GET['f-search'])
	searched_str = request.GET['f-search']

	context = {
		'faqs': faqs,
		'searched_str': searched_str
	}

	return render(request, 'faq/faq.html', context)
