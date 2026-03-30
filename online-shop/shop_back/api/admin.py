from django.contrib import admin
from .models import Category, Product

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ['name']
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description", "count", "is_active")
    search_fields = ['name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)



