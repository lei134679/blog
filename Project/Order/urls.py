from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create_shopcart_order/$', views.create_shopcart_order, name='create_shopcart_order'),
]