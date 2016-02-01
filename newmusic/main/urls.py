from django.conf.urls import include, url, patterns

from main.views import ArtistIndex, AboutIndex


urlpatterns = patterns('',
    url(r'^home/$', ArtistIndex.as_view(), name="artist_index"),
    url(r'^about/$', AboutIndex.as_view(), name="about_index"),
)
