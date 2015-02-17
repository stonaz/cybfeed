from django.conf.urls import patterns, url

from jsonSSL import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)