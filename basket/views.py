from django.shortcuts import render, redirect, reverse, HttpResponse


def show_basket(request):
	"""
	Renders all of the products currently in user's basket to the 
	basket.html page
	"""

	return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
	"""Add items to the shopping basket"""

	quantity = int(request.POST.get('quantity'))
	redirect_url = request.POST.get('redirect_url')
	basket = request.session.get('basket', {})

	if item_id in list(basket.keys()):
		basket[item_id] += quantity
	else:
		basket[item_id] = quantity

	request.session['basket'] = basket

	return redirect(redirect_url)


def update_basket(request, item_id):
	"""
	Updates the item quantity in the shopping basket
	or removes it completely
	"""

	quantity = int(request.POST.get('quantity'))
	basket = request.session.get('basket', {})

	if quantity > 0:
		basket[item_id] = quantity
	else:
		basket.pop(item_id)

	request.session['basket'] = basket

	return redirect(reverse('basket'))


def remove_from_basket(request, item_id):
	"""Removes item from the shopping basket"""

	try:
		basket = request.session.get('basket', {})

		basket.pop(item_id)

		request.session['basket'] = basket

		return HttpResponse(status=200)
	except Exception as e:
		return HttpResponse(status=500)
