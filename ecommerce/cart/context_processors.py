
from .cart import Cart

# this will return the default data from the cart
def cart(request):
    
    return {'cart': Cart(request)}











