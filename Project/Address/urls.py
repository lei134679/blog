from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^found_address/$', views.found_address, name='found_address'),
    url(r'^list_address/$', views.list_address, name='list_address'),
    url(r'^revise_address/(?P<id>\d+)/$', views.revise_address, name='revise_address'),
    url(r'^del_address/(?P<id>\d+)/$', views.del_address, name='del_address'),
]