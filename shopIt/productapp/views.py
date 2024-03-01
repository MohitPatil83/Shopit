from django.shortcuts import render
from productapp.models import Product
from django.db.models import Q

# Create your views here.
def homepage(request):
    #fetch active product from model product
    context={}
    
    #print(p)
    context['data']=Product.objects.filter(is_active=1)
    return render(request,'productapp/index.html',context)

def product_detail(request):
    pid=request.GET['id']
    context={}
    context['data']=Product.objects.get(id=pid)
    return render(request,'productapp/detail.html',context)

def filterbycar(request):
    x=request.GET['q']
    context={}
   
    q1=Q(is_active=1)
    q2=Q(cat=x)
    context['data']=Product.objects.filter(q1 & q2)
    return render(request,'productapp/index.html',context)
def sortbyprice(request):
    x=request.GET['q']
    context={}
    if x == '0':
        col='price'
        #context['data']=product.objects.order_by('price').filter(is_active=1)
    else:
        col='-price'
        #context['data']=product.objects.order_by('-price').filter(is_active=1)
    context['data']=Product.objects.order_by(col).filter(is_active=1)
    return render(request,'productapp/index.html',context)

def range(request):
    min_value=request.GET['min']
    max_value=request.GET['max']
   
    context={}
    context['data']=Product.objects.filter(Q(is_active=1) & Q(price__gte=min_value) & Q(price__lte=max_value))
    return render(request,'productapp/index.html',context)
    
