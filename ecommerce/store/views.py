from django.shortcuts import render

from .models import Category
# Create your views here.

def store(request):
    
    return render(request, 'store/store.html')

# nav bar categories, will be availible in all pages.
def categories(request):
    
    all_categories = Category.objects.all() 
    
    return {'all_categories': all_categories}


