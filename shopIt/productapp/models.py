from django.db import models

# Create your models here.
class Product(models.Model):
    CAT=((1,'Mobile'),(2,'Shoes'),(3,'Cloths'))
    name=models.CharField(max_length=50,verbose_name="Product Name")
    detail=models.CharField(max_length=500,verbose_name="Description")
    price=models.IntegerField()
    cat=models.IntegerField(verbose_name="Category",choices=CAT)
    is_active=models.BooleanField(default=1,verbose_name="Status")
    path=models.ImageField(upload_to='photos/')
