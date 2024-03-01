from django.urls import path
from productapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.homepage),
    path('detail',views.product_detail),
    path('filter',views.filterbycar),
    path('sort',views.sortbyprice),
    path('range',views.range),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
