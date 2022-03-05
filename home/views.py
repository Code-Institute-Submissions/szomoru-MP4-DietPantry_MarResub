from django.shortcuts import render

# Create your views here.


def index(request):
    """ this view returns to the index page """

    return render(request, 'home/index.html')

def keto(request):
    """ this view returns to the keto page """

    return render(request, 'home/keto.html')
