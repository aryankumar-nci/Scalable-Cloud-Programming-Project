from django.contrib import admin

# Register your models here.

from .models import Category, Product

#for prepopulated field in the Category field in admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug':('name',)}
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug':('title',)}
    
    
    