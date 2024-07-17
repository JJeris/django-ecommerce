from store.models import Product

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
        
    def add(self, product, quantity):
        """
        Adds a product to the session key.

        Args:
            product (_type_): _description_
        """        
        product_id = str(product.id)
        product_qty = str(quantity)
        
        # Have they already added it to the cart
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)
        
        self.session.modified = True
    
    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        # Get the product ids from the cart.
        product_ids = self.cart.keys()
        
        # Use ids to lookup products in the database model.
        products = Product.objects.filter(id__in=product_ids)
        
        # Returns the filtered products.
        return products
        
    def get_quants(self):
        quantities = self.cart
        return quantities
        
        
        