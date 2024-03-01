from django.shortcuts import render
from .models import Order
from cartapp.models import Cart
import random
# Create your views here.
def generateid():
    id=random.randrange(1000,9999)
    o=Order.objects.filter(order_id=id)
    if len(o)==0:
        return id
    else:
        generateid()

def homeorder(request):
    order_id=generateid()
  
    c=Cart.objects.filter(uid=request.user.id)
    #print(c)
    for x in c:
        o=Order.objects.create(order_id=order_id,pid=x.pid,uid=x.uid)
        o.save()
        x.delete()
    o=Order.objects.filter(uid=request.user.id)
    sum=0
    for x in o:
        sum=sum+(x.qty*x.pid.price)
    context={}
    context['data']=o
    context['total']=sum
    context['items']=len(o)
    return render(request,'orderapp/order.html',context)
