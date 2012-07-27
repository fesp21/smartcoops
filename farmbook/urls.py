from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', 'index'),
    url(r'^$', 'views.show', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^process/', 'views.process'),
    )
