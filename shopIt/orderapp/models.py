
from django.db import models

# Create your models here.
from productapp.models import Product
from django.contrib.auth.models import User

class Order(models.Model):
    order_id=models.IntegerField()
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column="pid")
    qty=models.IntegerField(default=1)