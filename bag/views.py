from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ this view renders the bag content page """
    return render(request, 'bag/bag.html')
