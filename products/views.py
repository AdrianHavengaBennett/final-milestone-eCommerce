from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product
from categories.models import Category


def show_products(request):
	"""
	Renders all of the products to the index.html page
	with pagination
	"""

	products = Product.objects.all()
	
	# products = Product.objects.all().order_by('price')
	# products = Product.objects.all().order_by('-price')
	# products = Product.objects.all().order_by('name')
	# products = Product.objects.all().order_by('-name')

	paginator = Paginator(products, per_page=2)
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)

	if page.has_next():
		next_url = f'?page={page.next_page_number()}'
	else:
		next_url = ''

	if page.has_previous():
		previous_url = f'?page={page.previous_page_number()}'
	else:
		previous_url = ''

	context = {
		'page': page,
		'next_url': next_url,
		'previous_url': previous_url
	}

	return render(request, 'products/index.html', context)


def sort_low_high(request):
	products = Product.objects.all().order_by('price')

	paginator = Paginator(products, per_page=2)
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)

	if page.has_next():
		next_url = f'?page={page.next_page_number()}'
	else:
		next_url = ''

	if page.has_previous():
		previous_url = f'?page={page.previous_page_number()}'
	else:
		previous_url = ''

	context = {
		'page': page,
		'next_url': next_url,
		'previous_url': previous_url
	}

	return render(request, 'products/index.html', context)


def sort_high_low(request):
	products = Product.objects.all().order_by('-price')
	
	paginator = Paginator(products, per_page=2)
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)

	if page.has_next():
		next_url = f'?page={page.next_page_number()}'
	else:
		next_url = ''

	if page.has_previous():
		previous_url = f'?page={page.previous_page_number()}'
	else:
		previous_url = ''

	context = {
		'page': page,
		'next_url': next_url,
		'previous_url': previous_url
	}

	return render(request, 'products/index.html', context)


def sort_a_z(request):
	products = Product.objects.all().order_by('name')
	
	paginator = Paginator(products, per_page=2)
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)

	if page.has_next():
		next_url = f'?page={page.next_page_number()}'
	else:
		next_url = ''

	if page.has_previous():
		previous_url = f'?page={page.previous_page_number()}'
	else:
		previous_url = ''

	context = {
		'page': page,
		'next_url': next_url,
		'previous_url': previous_url
	}

	return render(request, 'products/index.html', context)


def sort_z_a(request):
	products = Product.objects.all().order_by('-name')
	
	paginator = Paginator(products, per_page=2)
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)

	if page.has_next():
		next_url = f'?page={page.next_page_number()}'
	else:
		next_url = ''

	if page.has_previous():
		previous_url = f'?page={page.previous_page_number()}'
	else:
		previous_url = ''

	context = {
		'page': page,
		'next_url': next_url,
		'previous_url': previous_url
	}

	return render(request, 'products/index.html', context)



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
