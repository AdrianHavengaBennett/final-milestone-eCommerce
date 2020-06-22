from django.shortcuts import render
from django.core.paginator import Paginator
from products.models import Product
from products.views import do_pagination


def sort_low_high(request):
	context = do_pagination(request, products=Product.objects.all().order_by('price'))

	return render(request, 'products/index.html', context)


def sort_high_low(request):
	context = do_pagination(request, products=Product.objects.all().order_by('-price'))

	return render(request, 'products/index.html', context)


def sort_a_z(request):
	context = do_pagination(request, products=Product.objects.all().order_by('name'))

	return render(request, 'products/index.html', context)


def sort_z_a(request):
	context = do_pagination(request, products=Product.objects.all().order_by('-name'))

	return render(request, 'products/index.html', context)
