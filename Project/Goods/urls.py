from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^add_goods/$', views.add_goods, name='add_goods'),
    url(r'^list_goods/$', views.list_goods, name='list_goods'),
    url(r'^revise_goods/(?P<id>\d+)/$', views.revise_goods, name='revise_goods'),
    url(r'^del_goods/(?P<id>\d+)/$', views.del_goods, name='del_goods'),
    url(r'^details_goods/$', views.details_goods, name='details_goods'),
]