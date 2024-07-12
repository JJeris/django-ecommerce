from django.shortcuts import render, redirect
from . models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . forms import SignUpForm
from django import forms

def category(request, name):
    # Replace hyphen with spaces.
    # Note: if the category has hyphen, then you'll need to handle that.
    name = name.replace('-', ' ')
    # Grab the category from the url.
    try:
        # Look up the category.
        category = Category.objects.get(name=name)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})
    except:
        messages.success(request, ('That category does not exist. Badio!'))
        return redirect('home')
        
    

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})

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
    
    logout(request)
    messages.success(request, ('You have been logged out. Coolio!'))
    return redirect('home')

def register_user(request):
    """
    The user registration page.

    Args:
        request (_type_): _description_
    """
    
    form = SignUpForm() # Gets added to the context dictionary.
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid() == True:
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # login user.
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You have registered successfully. Coolio!'))
            return redirect('home')
        else:
            messages.success(request, ('Could not register your account. Badio!'))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})

