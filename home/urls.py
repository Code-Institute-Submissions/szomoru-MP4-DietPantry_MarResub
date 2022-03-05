from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('keto/', views.keto, name='keto'),
    path('lowcarb/', views.lowcarb, name='lowcarb'),
    path('highprotein/', views.highprotein, name='highprotein'),
    path('mediterranean/', views.mediterranean, name='mediterranean'),
]
