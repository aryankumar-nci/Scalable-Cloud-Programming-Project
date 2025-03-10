from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
# Create your views here.

from . models import ShippingAddress, Order, OrderItem

from cart.cart import Cart


from django.http import JsonResponse


def checkout(request):

    # Users with accounts -- Pre-fill the form

    if request.user.is_authenticated:

        try:

            # Authenticated users WITH shipping information 

            shipping_address = ShippingAddress.objects.get(user=request.user.id)

            context = {'shipping': shipping_address}

            


            return render(request, 'payment/checkout.html', context=context)


        except:

            # Authenticated users with NO shipping information

            return render(request, 'payment/checkout.html')

    else:
            
        # Guest users

        return render(request, 'payment/checkout.html')



from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import ShippingAddress, Order, OrderItem
from cart.cart import Cart

def complete_order(request):
    if request.POST.get('action') == 'post':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')

        shipping_address = f"{address1}\n{address2}\n{city}\n{state}\n{zipcode}"

        cart = Cart(request)
        total_cost = cart.get_total()

        if request.user.is_authenticated:
            order = Order.objects.create(
                full_name=name, email=email, shipping_address=shipping_address,
                amount_paid=total_cost, user=request.user
            )
        else:
            order = Order.objects.create(
                full_name=name, email=email, shipping_address=shipping_address,
                amount_paid=total_cost
            )

        for item in cart:
            OrderItem.objects.create(
                order=order, Product=item['product'], quantity=item['qty'],
                price=item['price'], user=request.user if request.user.is_authenticated else None
            )

        # Correctly clear the cart
        cart.cart = {}  # Instead of cart.clear()

        return JsonResponse({'success': True, 'order_id': order.id})

def order_receipt(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    
    context = {
        'order': order,
        'order_items': order_items
    }
    
    return render(request, 'payment/order-receipt.html', context)