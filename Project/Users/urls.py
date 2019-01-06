from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^regist_user/$', views.regist_user, name='regist_user'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^data_user/$', views.data_user, name='data_user'),
    url(r'^data_pwd/$', views.data_pwd, name='data_pwd'),
    url(r'^data_data/$', views.data_data, name='data_data'),
    url(r'^index/$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^send_message/$', views.send_message, name='send_message'),

]