from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
import requests

from .models import ShippingAddress, Order, OrderItem
from cart.cart import Cart

# PDF Generation API URL
PDF_API_URL = "http://54.167.76.195/api/generate_pdf"

def checkout(request):
    if request.user.is_authenticated:
        try:
            shipping_address = ShippingAddress.objects.get(user=request.user.id)
            context = {'shipping': shipping_address}
            return render(request, 'payment/checkout.html', context)
        except ShippingAddress.DoesNotExist:
            pass
    return render(request, 'payment/checkout.html')

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

def download_order_receipt(request, order_id):
    """
    Generate and return the order receipt as a downloadable PDF.
    """
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderItem.objects.filter(order=order)

    # Prepare JSON payload for the API
    report_data = {
        "report_title": "Order Receipt",
        "order_id": str(order.id),
        "name": order.full_name,
        "email": order.email,
        "shipping_address": order.shipping_address,
        "total": str(order.amount_paid),
        "report_description": "Thank you for your purchase! Below are the details of your order.",
        
        # ✅ Corrected header format (Dictionary instead of list)
        "report_table_data_header": {
            "column1": "Product Name",
            "column2": "Quantity",
            "column3": "Price",
            "column4": "Total Price"
        },

        # ✅ Ensuring list of dictionaries for table body
        "report_table_data_body": [
            {
                "column1": item.Product.title,
                "column2": str(item.quantity),
                "column3": f"€{item.price}",
                "column4": f"€{item.quantity * item.price}"
            }
            for item in order_items
        ],
    }

    try:
        response = requests.post(PDF_API_URL, json=report_data)
        if response.status_code == 200:
            pdf_content = response.content
            response = HttpResponse(pdf_content, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="order_receipt_{order.id}.pdf"'
            return response
        else:
            return JsonResponse({"error": f"Failed to generate PDF. Response: {response.text}"}, status=500)
    except requests.RequestException as e:
        return JsonResponse({"error": f"PDF API unavailable: {str(e)}"}, status=500)
