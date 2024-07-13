from django.shortcuts import render, get_object_or_404
from . cart import Cart
from store.models import Product
from django.http import JsonResponse

def  cart_summary(request):
    """
    _summary_

    Args:
        request (_type_): _description_
    """
    
    return render(request, "cart_summary.html", {})

def  cart_add(request):
    # Get the cart.
    cart = Cart(request)
    # test for post.
    if request.POST.get('action') == 'post':
        # Get the data
        product_id = int(request.POST.get('product_id'))
        # lookup product in DB
        product = get_object_or_404(Product, id=product_id)
        # Save to session.
        cart.add(product=product)
        
        # Get Cart Qty
        cart_quantity = cart.__len__()
        
        # Return response
        # response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty': cart_quantity}) ##
        return response
    
    return     

def  cart_delete(request):
    pass  
def  cart_update(request):
    pass