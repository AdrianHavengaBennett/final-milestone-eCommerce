from django.shortcuts import render
from .models import Product


def show_products(request):
	"""Renders all of the products to the index.html page"""

	products = Product.objects.all()

	return render(request, 'products/index.html', {'products': products})
