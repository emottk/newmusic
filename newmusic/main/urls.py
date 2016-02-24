from django.conf.urls import url, patterns

from newmusic.main import views


urlpatterns = patterns('',
    url(r'^$', views.ArtistIndex.as_view(), name="explore"),
    url(r'^about/$', views.AboutIndex.as_view(), name="about"),
    url(r'^artist/(?P<artist>[\w.@+-]+)/$', views.ArtistPage.as_view(), name="artist_page"),
    url(r'^opinion/delete/(?P<pk>\d+)$', views.OpinionDelete.as_view(), name="opinion_delete"),
)
