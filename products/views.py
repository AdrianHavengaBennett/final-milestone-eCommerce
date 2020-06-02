from django.shortcuts import render
from .models import Product


def show_products(request):
	"""Renders all of the products to the index.html page"""

	products = Product.objects.all()

	return render(request, 'products/index.html', {'products': products})


def show_product_detail(request, id):
	"""Renders the product details to the product_details.html page"""

	product = Product.objects.get(pk=id)

	return render(request, 'products/product_detail.html', {'product': product})
