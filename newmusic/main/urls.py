from django.conf.urls import include, url, patterns

from main.views import ArtistIndex, AboutIndex, ArtistPage


urlpatterns = patterns('',
    url(r'^home/$', ArtistIndex.as_view(), name="explore"),
    url(r'^about/$', AboutIndex.as_view(), name="about"),
    url(r'^artist/(?P<artist>[\w.@+-]+)/$', ArtistPage.as_view(), name="artist_page"),
)
