from django.shortcuts import render,redirect
from cartapp.models import Cart
from django.contrib.auth.models import User
from productapp.models import Product
from django.db.models import Q 

# Create your views here.
def homecart(request):
    context={}
    if request.user.is_authenticated:
        

        c=Cart.objects.filter(uid=request.user.id)
        #print(c)
        sum=0
        for x in c:
            #print(x)
            #print("Quantity",x.qty)
            #print("Price per product",x.pid.price)
            sum=sum+(x.qty*x.pid.price)
            #print(sum)
        context['data']=c
        context['total']=sum
        context['items']=len(c)
        return render(request,'cartapp/cart.html',context)
    else:
        return redirect('/authapp/login')

def add_to_cart(request):
    context={}
    if request.user.is_authenticated:
        pid=request.GET['id']
        user_id=request.user.id
        uobj=User.objects.get(id=user_id)
        pobj=Product.objects.get(id=pid)
        context['data']=pobj
      
        try:
              q1=Q(uid=uobj)
              q2=Q(pid=pobj)
              c=Cart.objects.get(q1 & q2)
              context['vmsg']="Product Already Exists in cart"
        except Exception:
            c=Cart.objects.create(uid=uobj,pid=pobj)
            c.save()
            context['success']="Product Successfully added in the cart"
         
        return render(request,'productapp/detail.html',context)
    else:
        return redirect('/authapp/login')
def updateqty(request):
    #fetch get request details
    q=request.GET['q']
    cid=request.GET['cid']
    c=Cart.objects.filter(id=cid)
    if q=='1':
        
        temp=c[0].qty+1
    else:
        
        if c[0].qty>1:
            temp=c[0].qty-1

        else:
            temp=1
    c.update(qty=temp)

    
    return redirect('/cartapp/')

