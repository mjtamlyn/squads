from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views


urlpatterns = patterns('',
    url('^$', views.Home.as_view(), name='home'),

    url('^sessions/$', views.SessionList.as_view(), name='session-list'),
    url('^sessions/add/$', views.SessionAdd.as_view(), name='session-add'),
    url('^sessions/(?P<pk>\d+)/$', views.SessionEdit.as_view(), name='session-edit'),
    url('^sessions/(?P<pk>\d+)/delete/$', views.SessionDelete.as_view(), name='session-delete'),

    url('^admin/', include(admin.site.urls)),
    url('', include('social_auth.urls')),
)
