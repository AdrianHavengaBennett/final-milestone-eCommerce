import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product
from shows.models import ShowsTickets
from click_and_collect.models import ClickCollectLocations


class Order(models.Model):
	order_number = models.CharField(max_length=32, null=False, editable=False)
	full_name = models.CharField(max_length=50, null=False, blank=False)
	email = models.EmailField(max_length=254, null=False, blank=False)
	phone_number = models.CharField(max_length=20, null=False, blank=False)
	postcode = models.CharField(max_length=20, null=True, blank=True)
	town_or_city = models.CharField(max_length=40, null=False, blank=False)
	street_address1 = models.CharField(max_length=80, null=False, blank=False)
	street_address2 = models.CharField(max_length=80, null=True, blank=True)
	county = models.CharField(max_length=40, null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True)
	DELIVER = 'deliver'
	CLICK_AND_COLLECT = 'click&collect'
	DELIVERY_CHOICES = [
		(DELIVER, 'deliver'),
		(CLICK_AND_COLLECT, 'click&collect'),
	]
	delivery_option = models.CharField(
		max_length=32,
		choices=DELIVERY_CHOICES,
		default=DELIVER,
		null=False,
		blank=False,
	)
	BEN = "Ben's Hardware"
	POST_OFFICE = 'Pembroke Park Post Office'
	CLICK_AND_COLLECT_CHOICES = [
		(BEN, "Ben's Hardware"),
		(POST_OFFICE, 'Pembroke Park Post Office'),
	]
	click_and_collect_option = models.CharField(
		max_length=80,
		choices=CLICK_AND_COLLECT_CHOICES,
		null=True,
		blank=True,
	)
	delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
	products_total = models.DecimalField(max_digits=6, decimal_places=2, null=True, default=0)
	tickets_total = models.DecimalField(max_digits=6, decimal_places=2, null=True, default=0)
	order_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
	grand_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)

	def _generate_order_number(self):
		"""Generate a random, unique order number using UUID"""

		return uuid.uuid4().hex.upper()

	def update_total(self):
		"""Update grand total each time a line item is added,
		accounting for delivery costs.
		"""

		self.products_total = (self.productlineitems.aggregate(
			Sum('productlineitems_total'))['productlineitems_total__sum']) or 0
		self.tickets_total = (self.ticketlineitems.aggregate(
			Sum('ticketlineitems_total'))['ticketlineitems_total__sum']) or 0
		self.order_total = self.products_total + self.tickets_total
		self.delivery_cost = settings.STANDARD_DELIVERY_CHARGE if self.delivery_option == 'deliver' else 0
		self.grand_total = self.order_total + self.delivery_cost
		self.save()

	def save(self, *args, **kwargs):
		"""Override the original save method to set the order number
		if it hasn't been set already and also to update the delivery
		charge if delivery option has been changed and no additional line
		items added to call update_total()
		"""

		self.delivery_cost = settings.STANDARD_DELIVERY_CHARGE if self.delivery_option == 'deliver' else 0

		if not self.order_number:
			self.order_number = self._generate_order_number()
		super().save(*args, **kwargs)

	def __str__(self):
		return self.order_number


class OrderLineProductItem(models.Model):
	order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='productlineitems')
	product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
	quantity = models.IntegerField(null=False, blank=False, default=0)
	productlineitems_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

	def save(self, *args, **kwargs):
		"""Override the original save method to set the lineproductitem total
		and update the order total.
		"""

		self.productlineitems_total = self.product.price * self.quantity
		super().save(*args, **kwargs)

	def __str__(self):
		return f'{self.product} on order {self.order.order_number}'


class OrderLineTicketItem(models.Model):
	order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='ticketlineitems')
	ticket = models.ForeignKey(ShowsTickets, null=False, blank=False, on_delete=models.CASCADE)
	quantity = models.IntegerField(null=False, blank=False, default=0)
	ticketlineitems_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

	def save(self, *args, **kwargs):
		"""Override the original save method to set the lineticketitem total
		and update the order total.
		"""

		self.ticketlineitems_total = self.ticket.price * self.quantity
		super().save(*args, **kwargs)

	def __str__(self):
		return f'{self.ticket} on order {self.order.order_number}'
