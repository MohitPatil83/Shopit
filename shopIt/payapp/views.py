from django.shortcuts import render,HttpResponse,redirect
from orderapp.models import Order
import razorpay
from django.core.mail import send_mail

# Create your views here.


def make_payment(request):
    o=Order.objects.filter(uid=request.user.id)
    sum=0
    for x in o:
        sum=sum+(x.pid.price*x.qty)
    
    #print(sum)
   
    tot=sum*100                                                                                                                    
    client = razorpay.Client(auth=("rzp_test_Yx2U1O5BE8be8N", "gDv6trPtGJYqphU1EzbrSrjr"))

    data = { "amount": tot, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)
    #print(payment)
    context={}
    context['payment']=payment

    return render(request,'payapp/pay.html',context)
def sendmail(request):
    payid=request.GET['pay_id']
    orderid=request.GET['order_id']
    sign=request.GET['sign']
    #print(payid)
    #print(orderid)
    #print(sign)
    msg="Order Placed Successfully.Details are Payment id is"+payid+"order id is"+orderid
    send_mail(
              "Order Details",
              msg,
              "mohitpatil5995@gmaill.com",
              ["patilmohit519@gmail.com"],
              fail_silently=False,
              )

    return HttpResponse("Email sended")

    