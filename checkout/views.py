from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.models import User
from click_and_collect.models import ClickCollectLocations
from .forms import OrderForm
from .models import OrderLineProductItem, OrderLineTicketItem, Order
from basket.contexts import basket_contents, do_db_query
import stripe


def get_location_info(request):
	if request.method == 'GET' and request.is_ajax():
		location = request.GET.get('location')
		try:
			cc_location = ClickCollectLocations.objects.get(
				location_name__icontains=location
			)
		except Exception as e:
			return JsonResponse({'success':False}, status=400)

		location_info = {
			'phone_number': cc_location.location_phone,
			'street_address1': cc_location.street_address1,
			'street_address2': cc_location.street_address2,
			'town_or_city': cc_location.town_or_city,
			'postcode': cc_location.postcode,
		}

		return JsonResponse({'location_info': location_info}, status=200)

	return JsonResponse({'success': False}, status=400)


def checkout(request):
	stripe_public_key = settings.STRIPE_PUBLIC_KEY
	stripe_secret_key = settings.STRIPE_SECRET_KEY

	if request.method == "POST":
		basket = request.session.get('basket', {})
		form_data = {
			'full_name': request.POST['full_name'],
			'email': request.POST['email'],
			'phone_number': request.POST['phone_number'],
			'postcode': request.POST['postcode'],
			'town_or_city': request.POST['town_or_city'],
			'street_address1': request.POST['street_address1'],
			'street_address2': request.POST['street_address2'],
			'county': request.POST['county'],
			'delivery_option': request.POST['delivery_option'],
			'click_and_collect_option': request.POST['click_and_collect_option'],
		}
		order_form = OrderForm(form_data)
		
		if order_form.is_valid():
			order = order_form.save()
			for item_id, item_data in basket.items():
				basket_obj = do_db_query(request, item_id=item_id)
				if '@' in str(basket_obj):
					order_line_ticket_item = OrderLineTicketItem(
						order=order,
						ticket=basket_obj,
						quantity=item_data,
					)
					order_line_ticket_item.save()
				else:
					order_line_product_item = OrderLineProductItem(
						order=order,
						product=basket_obj,
						quantity=item_data,
					)
					order_line_product_item.save()

			return redirect(reverse('checkout-success', args=[order.order_number]))
		else:
			messages.error(request, 'There was an error with your form \
				Please double check your information.')

	else:
		basket = request.session.get('basket', {})
		if not basket:
			messages.error(request, "Basket is currently empty.")
			return redirect(reverse('products-home'))

		current_basket = basket_contents(request)
		total = current_basket['grand_total']
		stripe_total = round(total * 100)
		stripe.api_key = stripe_secret_key
		intent = stripe.PaymentIntent.create(
			amount=stripe_total,
			currency=settings.STRIPE_CURRENCY,
		)

		if request.user.is_authenticated:
			try:
				user = User.objects.get(email=request.user.email)
				order_form = OrderForm(initial={
					'full_name': f'{user.first_name} {user.last_name}',
					'email': user.email
				})
			except User.DoesNotExist:
				order_form = OrderForm()	
		else:
			order_form = OrderForm()

	if not stripe_public_key:
		messages.warning(request, 'Stripe public key is missing. \
			Did you forget to set it in your environment?')

	context = {
		'order_form': order_form,
		'stripe_public_key': stripe_public_key,
		'client_secret': intent.client_secret,
	}

	return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
	"""Handles successful checkouts"""

	order = get_object_or_404(Order, order_number=order_number)
	messages.success(request, f'Order successfully processed! \
		Your order number is {order.order_number}. A confirmation email \
		will be sent to {order.email}.')

	if 'basket' in request.session:
		del request.session['basket']

	return render(request, 'checkout/checkout_success.html', {'order': order})
