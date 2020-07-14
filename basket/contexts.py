from django.shortcuts import get_object_or_404
from django.conf import settings
from decimal import Decimal
from products.models import Product
from shows.models import ShowsTickets


def do_db_query(request, item_id):
	"""Helper function avoids variable scope UnboundLocalError issues while 
	using if else and assignment when determining which model to query
	"""

	# ShowsTickets objects each have a uuid custom pk,
	# which contains numerous dashes, whereas Django's
	# default pks are whole integers
	if '-' in item_id:  
		query = get_object_or_404(ShowsTickets, pk=item_id)
	else:
		query = get_object_or_404(Product, pk=item_id)

	return query


def basket_contents(request):

	basket_items = []
	product_total = 0
	sub_total = 0
	grand_total = 0
	product_count = 0
	cc_free_delivery = 0
	standard_delivery = settings.STANDARD_DELIVERY_CHARGE

	basket = request.session.get('basket', {})

	for item_id, quantity in basket.items():

		basket_obj = do_db_query(request, item_id=item_id)

		product_total = quantity * basket_obj.price
		grand_total += quantity * basket_obj.price
		product_count += quantity
		basket_items.append({
			'item_id': item_id,
			'quantity': quantity,
			'basket_obj': basket_obj,
			'product_total': product_total
		})

	if standard_delivery:
		grand_total += standard_delivery

	sub_total = grand_total - standard_delivery

	context = {
		'basket_items': basket_items,
		'product_count': product_count,
		'sub_total': sub_total,
		'product_total': product_total,
		'grand_total': grand_total,
		'standard_delivery': standard_delivery,
		'cc_free_delivery': cc_free_delivery,
	}

	return context
