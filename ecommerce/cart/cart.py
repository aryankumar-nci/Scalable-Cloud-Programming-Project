# session 
class Cart():

    def __init__(self,request):
        
        self.session = request.session
        
        #returning user - get user's session key
        
        cart = self.session.get('session_key')
        
        #new user - generate a session
        
        if 'session_key' not in request.session:
            
            cart = self.session['session_key'] = {}
            
        # cart will remember if a user have product in his cart or not.    
        self.cart = cart 
     
    
    def add(self, product, product_qty):
        
        product_id = str(product.id)
        
        if product_id in self.cart:
            
            self.cart[product_id]['qty']=product_qty
            
        else:
            
            self.cart[product_id] = {'price':str(product.price),'qty':product_qty}
        
        self.session.modified = True
        
    # this will remember the cart item in current session
    
    def __len__(self):
        
        return sum(item['qty'] for item in self.cart.values())
         
        
                