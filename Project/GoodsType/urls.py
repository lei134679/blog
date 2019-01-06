from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^set_goodstype/$', views.set_goodstype, name='set_goodstype'),
    url(r'^list_goodstype/$', views.list_goodstype, name='list_goodstype'),
    url(r'^revise_goodstype/(?P<id>\d+)$', views.revise_goodstype, name='revise_goodstype'),
    url(r'^del_goodstype/(?P<id>\d+)$', views.del_goodstype, name='del_goodstype'),
]