from django.contrib import admin
from productapp.models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
   
   list_display=['name','detail','price','cat','is_active']
   list_filter=['cat','is_active']

admin.site.register(Product,ProductAdmin)