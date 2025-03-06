from django.db import models

# this will allow to create own url for products
from django.urls import reverse

class Category(models.Model):
    
    name = models.CharField(max_length=250, db_index=True)
    
    slug = models.SlugField(max_length=250,unique=True)
    
    class Meta:
        
        verbose_name_plural = 'categories'
    
    #Category (1) , category (2) --shirts , Shoes   
    def __str__(self):
        
        return self.name  
      
    def get_absolute_url(self):
        return reverse('list-category', args=[self.slug])
    
class Product(models.Model):
    
    #forign key here to linK products to the category
    # if the category is deleted then product associated with it would also deleted.
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)
    
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
    
    # for custom url for products, will get to the product individual page.
    def get_absolute_url(self):
        return reverse('product-info', args=[self.slug])
    