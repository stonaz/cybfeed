from django.conf.urls import patterns, url

from jsonSSL import views

urlpatterns = patterns('',
    url(r'^$', views.socket_api, name='socket_api'),
    url(r'^update-config', views.update_api, name='update_api'),
    url(r'^get_feed_data', views.get_feed_data_api, name='get_feed_data_api'),
    #url(r'^$', views.index, name='index'),
)