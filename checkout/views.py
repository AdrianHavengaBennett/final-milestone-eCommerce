from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
	basket = request.session.get('basket', {})
	if not basket:
		messages.error(request, "Basket is currently empty.")
		return redirect(reverse('products-home'))

	order_form = OrderForm()
	context = {
		'order_form': order_form,
		'stripe_public_key': 'pk_test_H9vI3qzbKhdeuIIjaCR6LHj200ONcwKfRP',
		'client_secret': 'test_client_secret',
	}

	return render(request, 'checkout/checkout.html', context)
