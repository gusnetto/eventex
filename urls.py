# -*- coding: utf-8 -*- 
from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    # Examples:
    # url(r'^$', 'eventex.views.home', name='home'),
    # url(r'^eventex/', include('eventex.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

   
    url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'core.views.homepage'),
    (r'^inscricao/', include('subscription.urls', namespace='subscription')),
)

urlpatterns += staticfiles_urlpatterns()
