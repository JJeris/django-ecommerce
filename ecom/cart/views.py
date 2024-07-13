from django.shortcuts import render


def  cart_summary(request):
    """
    _summary_

    Args:
        request (_type_): _description_
    """
    
    return render(request, "cart_summary.html", {})

def  cart_add(request):
    pass
def  cart_delete(request):
    pass  
def  cart_update(request):
    pass