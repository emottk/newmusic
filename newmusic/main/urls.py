from django.conf.urls import include, url, patterns

from main.views import ArtistIndex


urlpatterns = patterns('',
    url(r'^$', ArtistIndex.as_view(), name="artist_index"),
)
