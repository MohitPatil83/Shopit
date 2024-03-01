from django.urls import path
from cartapp import views

urlpatterns = [
  path('',views.homecart),
  path('addcart/',views.add_to_cart),
  path('changeqty',views.updateqty),

]