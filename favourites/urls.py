from django.urls import path
from . import views


urlpatterns = [
    path('', views.favourite, name='favourite'),
    path('add_to_favourites/<product_id>', views.add_to_favourites, name='add_to_favourites'),
    path('remove_from_favourites/<product_id>', views.remove_from_favourites, name='remove_from_favourites'),
]