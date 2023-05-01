from django.contrib import admin
from apps.shop.models import Category, Product, CheckOut
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug":("name", )}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name", 
        "price", 
        "is_available", 
    ]
    list_filter = [
        "category", 
        "created"
    ]
    search_fields = [
        "name", 
    ]
    list_editable = [
        "is_available", 
    ]

@admin.register(CheckOut)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = [
        "name", 
        "surname", 
         
    ]