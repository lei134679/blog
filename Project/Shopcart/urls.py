from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^(?P<id>\w+)/add_shopcart/$', views.add_shopcart, name='add_shopcart'),
    url(r'^list_shopcart/$', views.list_shopcart, name='list_shopcart'),
    url(r'^del_shopcart/(?P<id>\d+)/$', views.del_shopcart, name='del_shopcart'),
    url(r'^shopcart/$', views.shopcart, name='shopcart'),
]