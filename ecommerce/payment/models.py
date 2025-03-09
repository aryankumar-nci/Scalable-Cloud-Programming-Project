from django.db import models

# Create your models here.

from django.contrib.auth.models import User

from store.models import Product

class ShippingAddress(models.Model):
    
    full_name = models.CharField(max_length=300)
    
    email = models.EmailField(max_length=255)
    
    address1 = models.CharField(max_length=300)
    
    address2 = models.CharField(max_length=255)
    
    city = models.CharField(max_length=255)
    
    #optional
    
    state = models.CharField(max_length=255, null=True, blank=True)
    
    zipcode = models.CharField(max_length=300, null=True,blank=True)


    #Forign key 
    # If user deletes account then all information for shipping will be deleted.
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    
    class Meta:
        
        verbose_name_plural = 'Shipping Address'
        
    def __str__(self):
        
        return 'Shipping Address - ' + str(self.id)
    
    
#Order models--------------------------------------------------------

class Order(models.Model):
    
    full_name = models.CharField(max_length=300)
    
    email = models.EmailField(max_length=255)
    
    shipping_address = models.TextField(max_length=10000)
    
    #amount paid
    
    amount_paid = models.DecimalField(max_digits=8,decimal_places=2)
    
    date_ordered = models.DateTimeField(auto_now_add=True)
    
    #Forign-key 
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        
        return '0rder - #' + str(self.id)


#Order item models----------------

class OrderItem(models.Model):
    
    #forign key->
    
    order = models.ForeignKey(Order,on_delete=models.CASCADE, null=True)
    
    Product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    
    quantity = models.PositiveBigIntegerField(default=1)
    
    price = models.DecimalField(max_digits=8,decimal_places=2)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    
    def __str__(self):
        
        return '0rder item - #' + str(self.id)
    
    
      