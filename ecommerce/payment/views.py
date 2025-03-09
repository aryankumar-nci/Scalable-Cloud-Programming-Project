from django.shortcuts import render

from . models import ShippingAddress

# Create your views here.

def checkout(request):
    
    #users with account will be pre-filled the shipping details.
    
    if request.user.is_authenticated:
        
        try:
            #authenticated user WITH shipping information.
            
            shipping_address = ShippingAddress.objects.get(user=request.user.id)
            
            context = {'shipping': shipping_address}
            
            return render(request,'payment/checkout.html',context=context)
        
        except:
            
            #authenticated user with No shipping information.
            return render(request,'payment/checkout.html')
    else:   
        #for the guest users
        return render(request,'payment/checkout.html')
    
    
def complete_order(request):
    pass

def payment_success(request):
    
    return render(request,'payment/payment-success.html')

def payment_failed(request):
    
    return render(request,'payment/payment-failed.html')










