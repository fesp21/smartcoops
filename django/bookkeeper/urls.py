from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('bookkeeper.views',
    url(r'^$', 'index'),
)
