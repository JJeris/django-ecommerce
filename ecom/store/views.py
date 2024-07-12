from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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


def login_user(request):
    """
    The login page.

    Args:
        request (_type_): _description_
    """    
    # If they filled in the form, then do this.
    if request.method == 'POST':
        username = request.POST['username'] # Matches the 'name' attribute in the username input tag.
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, ('You have logged in. Coolio!'))
            return redirect('home')
        else:
            messages.success(request, ('Could not log you in. Badio!'))
            return redirect('login')
        
    # If they didn't fill out the form, then just give them the login page.
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    """
    The logout page.

    Args:
        request (_type_): _description_
    """    
    
    # return render(request, 'login.html', {})
    logout(request)
    messages.success(request, ('You have been logged out. Coolio!'))
    return redirect('home')


