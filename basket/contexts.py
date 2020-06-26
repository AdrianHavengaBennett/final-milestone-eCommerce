from django.shortcuts import get_object_or_404
from django.conf import settings
from decimal import Decimal
from products.models import Product


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
		product = get_object_or_404(Product, pk=item_id)
		product_total = quantity * product.price
		grand_total += quantity * product.price
		product_count += quantity
		basket_items.append({
			'item_id': item_id,
			'quantity': quantity,
			'product': product,
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
		'grand_total': grand_total
	}

	return context