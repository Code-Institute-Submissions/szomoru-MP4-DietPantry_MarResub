from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    This method update order total on LineItem
    Update/Create
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, **kwargs):
    """
    This method update order total on LineItem
    Delete
    """
    instance.order.update_total()
