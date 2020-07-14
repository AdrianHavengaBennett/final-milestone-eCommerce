from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from products.models import Product
from basket.contexts import do_db_query
from click_and_collect.models import ClickCollectLocations


def show_basket(request):
	"""Renders all of the products currently in user's basket to the 
	basket.html page
	"""

	location = 'Enter delivery details on next page, or choose click and collect.'

	if request.GET:
		if 'location' in request.GET:
			locationkey = request.GET['location']
			location = locationkey
			if locationkey == 'ben':
				location = ClickCollectLocations.objects.get(location_name__icontains='ben')
			elif locationkey == 'pembroke':
				location = ClickCollectLocations.objects.get(location_name__icontains='pembroke')


	return render(request, 'basket/basket.html', {'location': location})


def add_to_basket(request, item_id):
	"""Add items to the shopping basket. Calls on get_db_query
	helper function to ascertain which model to query
	"""

	product = do_db_query(request, item_id=item_id)

	quantity = int(request.POST.get('quantity'))
	redirect_url = request.POST.get('redirect_url')
	basket = request.session.get('basket', {})

	if item_id in list(basket.keys()):
		basket[item_id] += quantity
		messages.success(request, f'Updated {product} quantity to {basket[item_id]}')
	else:
		basket[item_id] = quantity
		messages.success(request, f'Added {product} to your basket')

	request.session['basket'] = basket

	return redirect(redirect_url)


def update_basket(request, item_id):
	"""Updates the item quantity in the shopping basket or
	removes it completely. Calls on get_db_query helper 
	function to ascertain which model to query
	"""

	product = do_db_query(request, item_id=item_id)

	quantity = int(request.POST.get('quantity'))
	basket = request.session.get('basket', {})

	if quantity > 0:
		basket[item_id] = quantity
		messages.success(request, f'Updated {product} quantity to {basket[item_id]}')
	else:
		basket.pop(item_id)
		messages.success(request, f'Removed {product} from your basket')

	request.session['basket'] = basket

	return redirect(reverse('basket'))


def remove_from_basket(request, item_id):
	"""Removes item from the shopping basket. Calls on get_db_query 
	helper function to ascertain which model to query
	"""

	product = do_db_query(request, item_id=item_id)

	try:
		basket = request.session.get('basket', {})

		basket.pop(item_id)
		messages.success(request, f'Removed {product} from your basket')

		request.session['basket'] = basket

		return HttpResponse(status=200)
	except Exception as e:
		messages.error(request, f'Error removing item: {e}')
		return HttpResponse(status=500)
