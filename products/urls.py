from django.urls import path

from . import views

urlpatterns = [

    path('product/(?P<product_id>\w+)',  views.product,  name= 'product'),
]
