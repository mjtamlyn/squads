from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views


urlpatterns = patterns('',
    url('^$', views.Home.as_view(), name='home'),

    url('^sessions/add/$', views.SessionAdd.as_view(), name='session-add'),

    url('^admin/', include(admin.site.urls)),
    url('', include('social_auth.urls')),
)
