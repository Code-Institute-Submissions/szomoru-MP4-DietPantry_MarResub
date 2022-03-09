from django.shortcuts import render

# Create your views here.


def index(request):
    """ this view returns to the index page """

    return render(request, 'home/index.html')


def keto(request):
    """ this view returns to the keto page """

    return render(request, 'home/keto.html')


def lowcarb(request):
    """ this view returns to the Low carb page """

    return render(request, 'home/lowcarb.html')


def highprotein(request):
    """ this view returns to the keto page """

    return render(request, 'home/highprotein.html')


def mediterranean(request):
    """ this view returns to the mediterranean page """

    return render(request, 'home/mediterranean.html')
