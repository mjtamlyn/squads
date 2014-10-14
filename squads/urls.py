from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views


urlpatterns = patterns('',
    url('^$', views.Home.as_view(), name='home'),

    url('^squads/$', views.SquadList.as_view(), name='squads'),
    url('^information/$', views.Information.as_view(), name='information'),

    url('^sessions/$', views.SessionList.as_view(), name='session-list'),
    url('^sessions/add/$', views.SessionAdd.as_view(), name='session-add'),
    url('^sessions/(?P<pk>\d+)/$', views.SessionEdit.as_view(), name='session-edit'),
    url('^sessions/(?P<pk>\d+)/delete/$', views.SessionDelete.as_view(), name='session-delete'),

    url('^scores/$', views.ScoreList.as_view(), name='score-list'),
    url('^scores/add/$', views.ScoreAdd.as_view(), name='score-add'),
    url('^scores/(?P<pk>\d+)/$', views.ScoreEdit.as_view(), name='score-edit'),
    url('^scores/(?P<pk>\d+)/delete/$', views.ScoreDelete.as_view(), name='score-delete'),

    url('^videos/$', views.VideoList.as_view(), name='video-list'),
    url('^videos/add/$', views.VideoAdd.as_view(), name='video-add'),
    url('^videos/(?P<pk>\d+)/$', views.VideoEdit.as_view(), name='video-edit'),
    url('^videos/(?P<pk>\d+)/delete/$', views.VideoDelete.as_view(), name='video-delete'),

    url('^archers/(?P<pk>\d+)/$', views.UserHistory.as_view(), name='user-history'),
    url('^archers/(?P<pk>\d+)/notes/add/$', views.CoachNoteAdd.as_view(), name='note-add'),

    url('^admin/', include(admin.site.urls)),
    url('', include('social_auth.urls')),
)
