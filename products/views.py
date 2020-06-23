from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product
from categories.models import Category


def do_pagination(request, products):
	"""
	Helper function creates pagination and sort data and returns
	data as a dict to be used as context dict in views
	"""

	sort = None
	direction = None

	if request.GET:
		if 'sort' in request.GET:
			sortkey = request.GET['sort']
			sort = sortkey
			if sortkey == 'name':
				sortkey = 'lower_name'
				products = products.annotate(lower_name=Lower('name'))

			if 'direction' in request.GET:
				direction = request.GET['direction']
				if direction == 'desc':
					sortkey = f'-{sortkey}'
			products = products.order_by(sortkey)

	current_sorting = f'{sort}_{direction}'

	paginator = Paginator(products, per_page=12)
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

	page_data = {
		'page': page,
		'next_url': next_url,
		'previous_url': previous_url,
		'current_sorting': current_sorting
	}

	return page_data


def show_products(request):
	"""
	Renders all of the products to the index.html page
	with pagination
	"""

	context = do_pagination(request, products=Product.objects.all())

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

	context = do_pagination(request, products=Product.objects.filter(category_name=id))

	for product in context['page'].object_list:
		category_name = product.category_name
		category_image = product.category_name.image.url
		category_id = product.category_name.id

	context['category_name'] = category_name
	context['category_image'] = category_image
	context['category_id'] = category_id

	return render(request, 'products/category_products.html', context)
