
from django.urls import path
from orderapp import views

urlpatterns = [
  path('',views.homeorder)
]