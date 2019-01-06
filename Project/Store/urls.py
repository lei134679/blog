from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^set_store/$', views.set_store, name='set_store'),
    url(r'^list_store/$', views.list_store, name='list_store'),
    url(r'^revise_store/(?P<id>\d+)/$', views.revise_store, name='revise_store'),
    url(r'^del_store/(?P<id>\d+)/$', views.del_store, name='del_store'),

]