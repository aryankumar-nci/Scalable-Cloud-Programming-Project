from django.db import models

class Category(models.Model):
    
    name = models.CharField(max_length=250, db_index=True)
    
    slug = models.SlugField(max_length=250,unique=True)
    
    class Meta:
        
        verbose_name_plural = 'categories'
    
    
    #Category (1) , category (2) --shirts , Shoes   
    def __str__(self):
        
        return self.name    
    
class Product(models.Model):
    
    title = models.CharField(max_length=250)
    
    brand = models.CharField(max_length=250, default='un-branded')
    
    description = models.TextField(blank=True)
    # slug for unique product
    slug = models.SlugField(max_length=255)
    
    price = models.DecimalField(max_digits=4,decimal_places=2)
    
    image = models.ImageField(upload_to='images/')
    
    
    class Meta:
        
        verbose_name_plural = 'products'
    
    
    #product(1) , product (2) --shirts , Shoes   
    def __str__(self):
        # returns product actual name instead of title only.
        return self.title   