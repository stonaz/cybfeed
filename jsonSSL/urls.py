from django.conf.urls import patterns, url

from jsonSSL import views

urlpatterns = patterns('',
    url(r'^$', views.socket_api, name='socket_api'),                 
    #url(r'^$', views.index, name='index'),
)