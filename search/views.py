from django.shortcuts import render
from blog.models import BlogPost
from products.models import Product


def blog_search(request):
	"""Does a search on the blog posts"""

	blog_posts = BlogPost.objects.filter(title__icontains=request.GET['b-search'])

	return render(request, 'blog/blog_home.html', {'posts': blog_posts})


def products_search(request):
	"""Does a search on all products"""

	products = Product.objects.filter(name__icontains=request.GET['p-search'])

	return render(request, 'products/index.html', {'products': products})
