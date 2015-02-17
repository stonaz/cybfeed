from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cyberfeed.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('ui.urls')),
    url(r'^socket/', include('jsonSSL.urls')),
    url(r'^admin/', include(admin.site.urls)),
)



