from django.shortcuts import render

# Create your views here.

def index(request):
    """ a view that displays index page """
    return render(request, "index.html")