from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from products.models import Product
from .models import Favourite


# Create your views here.
@login_required
def favourite(request):
    favourite = None
    try:
        favourite = Favourite.objects.get(user=request.user)
    except Favourite.DoesNotExist:
        pass

    context = {
        'favourite': favourite,
    }

    return render(request, 'favourites/favourites.html', context)


@login_required
def add_to_favourites(request, product_id):
    """
    Add products to the favourites for the registered user
    This function require login
    """
    product = get_object_or_404(Product, pk=product_id)

    # If favourite list is not exoiting it is going to create
    favourite, _ = Favourite.objects.get_or_create(user=request.user)

    # Adding product to the favourites
    favourite.products.add(product)
    messages.info(request, "A new product is added to your favourites")

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_favourites(request, product_id):
    """
    Remove product from the favourites for the registered user
    This function require login
    """
    favourite = Favourite.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    # Removinging product from the favourites
    favourite.products.remove(product)
    messages.info(request, "A product has been removed from your favourites")

    return redirect(request.META.get('HTTP_REFERER'))
