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
        