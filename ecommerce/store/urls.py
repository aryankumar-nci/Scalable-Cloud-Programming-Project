
from django.urls import path

from . import views 

urlpatterns = [
     #store main page
     path('',views.store, name='store'),
     
     # this will redirect to the individual product.
     path('product/<slug:product_slug>/', views.product_info, name='product-info'),
     
     # filters each product by individual category.
     path('search/<slug:category_slug>/', views.list_category, name='list-category'),
     
     #QR CODE API
     path("generate-qr-code/", views.generate_qr_code, name="generate-qr-code"),
     
]




