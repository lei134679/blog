from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add_goodsimage/(?P<id>\d+)/$', views.add_goodsimage, name='add_goodsimage'),
    url(r'^del_goodsimage/(?P<id>\d+)/$', views.del_goodsimage, name='del_goodsimage'),
]