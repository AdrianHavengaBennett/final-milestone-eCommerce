from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
	basket = request.session.get('basket', {})
	if not basket:
		messages.error(request, "Basket is currently empty.")
		return redirect(reverse('products-home'))

	order_form = OrderForm()

	return render(request, 'checkout/checkout.html', {'order_form': order_form})
