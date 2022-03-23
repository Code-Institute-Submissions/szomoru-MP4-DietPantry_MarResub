from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Create your models here.
class Favourite(models.Model):
    """
    Model to show the items on the user favourites list
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(
                Product, through="FavouriteItem",
                related_name='product_favourites'
                )

    def __str__(self):
        return f'Favourite({self.user})'


class FavouriteItem(models.Model):
    product = models.ForeignKey(Product,
                                null=False,
                                blank=False,
                                on_delete=models.CASCADE)
    favourite = models.ForeignKey(
                Favourite, null=False,
                blank=False, on_delete=models.CASCADE
                )

    def __str__(self):
        return self.product.name
