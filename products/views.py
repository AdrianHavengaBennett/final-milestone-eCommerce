from django.shortcuts import render


def show_products(request):
	return render(request, 'products/index.html', {'todo': 'All products/main page'})
