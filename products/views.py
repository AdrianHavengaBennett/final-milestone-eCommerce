from django.shortcuts import render
from .models import Product
from categories.models import Category


def show_products(request):
	"""Renders all of the products to the index.html page"""

	products = Product.objects.all()

	return render(request, 'products/index.html', {'products': products})


def show_product_detail(request, id):
	"""Renders the product details to the product_details.html page"""

	product = Product.objects.get(pk=id)

	return render(request, 'products/product_detail.html', {'product': product})


def show_category_products(request, id):
	"""
	Renders all the products with the clicked category 
	name to the category_products.html page
	"""

	products = Product.objects.filter(category_name=id)

	for product in products:
		category_name = product.category_name
		category_image = product.category_name.image.url

	context = {
		'products': products,
		'category_name': category_name,
		'category_image': category_image
	}

	return render(request, 'products/category_products.html', context)
