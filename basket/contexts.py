def basket_contents(request):

	basket_items = {}
	total = 0
	product_count = 0
	cc_free_delivery = 0
	standard_delivery = 20

	if cc_free_delivery:
		grand_total = total
	else:
		grand_total = total + standard_delivery

	context = {
		'basket_items': basket_items,
		'total': total,
		'product_count': product_count,
		'grand_total': grand_total
	}

	return context