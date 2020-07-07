from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineProductItem, OrderLineTicketItem


# not being called on update/create
@receiver(post_save, sender=OrderLineTicketItem)
@receiver(post_save, sender=OrderLineProductItem)
def update_on_save(sender, instance, created, **kwargs):
	"""Update order total on lineproductitem and
	lineticketitem update/create
	"""
	
	print('Hello, signals here!')
	instance.order.update_total()


# works fine and, when called, updates everything accordingly
@receiver(post_delete, sender=OrderLineTicketItem)
@receiver(post_delete, sender=OrderLineProductItem)
def update_on_save(sender, instance, **kwargs):
	"""Update order total on lineproductitem and
	lineticketitem delete"""

	print('Hello, signals here!')
	instance.order.update_total()


