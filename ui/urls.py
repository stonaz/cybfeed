from django.conf.urls import patterns, url

from ui import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^login2/$', views.user_login2, name='login2'),
)