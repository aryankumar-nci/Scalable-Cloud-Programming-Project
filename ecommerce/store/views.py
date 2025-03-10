from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.conf import settings

from .models import Category, Product

from django.shortcuts import get_object_or_404

def store(request):
    #brings all product from db to the frontpage
    all_products = Product.objects.all()
    
    context= {'my_products': all_products}
    
    return render(request, 'store/store.html', context)

# nav bar categories, will be availible in all pages.
def categories(request):
    
    all_categories = Category.objects.all() 
    
    return {'all_categories': all_categories}

#filter products based on category.
def list_category(request, category_slug=None):
    
    category = get_object_or_404(Category, slug=category_slug)

    products = Product.objects.filter(category=category)
    
    return render(request, 'store/list-category.html', {'category':category, 'products': products})

#get individual product from db

def product_info(request,product_slug):
    
    product = get_object_or_404(Product,slug=product_slug)
    
    context = {'product': product}

    return render(request, 'store/product-info.html', context)


#API function

def generate_qr_code(request):
    """
    Fetch QR code from the EC2-hosted API for the current page.
    """
    current_url = request.GET.get("url", "")
    
    if not current_url:
        return JsonResponse({"error": "URL is required"}, status=400)

    qr_api_url = f"{settings.QR_CODE_API_URL}{current_url}"

    try:
        response = requests.get(qr_api_url)
        if response.status_code == 200:
            return JsonResponse({"qr_code_url": qr_api_url})
        else:
            return JsonResponse({"error": "Failed to generate QR code"}, status=500)
    except requests.RequestException:
        return JsonResponse({"error": "QR Code API unavailable"}, status=500)







