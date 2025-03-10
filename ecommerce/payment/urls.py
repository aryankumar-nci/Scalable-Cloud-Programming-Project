from django.urls import path
from . import views 

urlpatterns = [
    path('checkout', views.checkout, name='checkout'),
    path('complete-order', views.complete_order, name='complete-order'),
    path('order-receipt/<int:order_id>/', views.order_receipt, name='order-receipt'),
]
