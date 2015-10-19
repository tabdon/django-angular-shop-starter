from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'core.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
)
