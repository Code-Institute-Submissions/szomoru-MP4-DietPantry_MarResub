from django.db import models

def index(request):
    """ this view returns to the product page """
    return render(request, 'products/products.html')
