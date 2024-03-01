from django.urls import path
from payapp import views

urlpatterns = [
  #path('',views.homeorder)
    path('',views.make_payment),
    path('sendmail',views.sendmail),
]