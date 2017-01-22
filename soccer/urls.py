from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^competitions/$', views.CompetitionListView.as_view(), name='competitions'),
    url(r'^competition/(?P<comp_id>\d+)/matches$', views.MatchesByCompetitionListView.as_view(), name='matches-by-competition'),
    url(r'^matches/$', views.MatchListView.as_view(), name='matches'),
    url(r'^match/(?P<pk>\d+)$', views.MatchDetailView.as_view(), name='match-detail'),
]
