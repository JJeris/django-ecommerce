from django.shortcuts import render
from .models import Product


def home(request):
    """
    The home page.

    Args:
        request (?): The request for the home page.

    Returns:
        home.html: The home page for the website.
    """    
    products = Product.objects.all
    return render(request, 'home.html', {'products': products})


def about(request):
    """
    The about me page.

    Args:
        request (_type_): _description_
    """    
    
    return render(request, 'about.html', {})

