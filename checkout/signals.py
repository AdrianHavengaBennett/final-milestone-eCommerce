from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Order, OrderLineProductItem, OrderLineTicketItem


@receiver(post_save, sender=OrderLineTicketItem)
@receiver(post_save, sender=OrderLineProductItem)
def update_on_save(sender, instance, created, **kwargs):
    """Update order total on lineproductitem and
    lineticketitem update/create
    """

    instance.order.update_total()


@receiver(post_delete, sender=OrderLineTicketItem)
@receiver(post_delete, sender=OrderLineProductItem)
def update_on_delete(sender, instance, **kwargs):
    """Update order total on lineproductitem and
    lineticketitem delete
    """

    instance.order.update_total()
