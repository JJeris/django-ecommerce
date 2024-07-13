class Cart():
    
    def __init__(self, request):
        self.session = request.session
        
        # Get the current session key
        cart = self.session.get('session_key')
        
        # If the user is new, no session key -> create one.
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
        # Make sure cart is available on all pages on site.
        self.cart = cart
        
    def add(self, product):
        """
        Adds a product to the session key.

        Args:
            product (_type_): _description_
        """        
        product_id = str(product.id)
        
        # Have they already added it to the cart
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
        
        self.session.modified = True