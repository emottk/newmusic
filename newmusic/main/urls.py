from django.conf.urls import include, url, patterns

from main.views import Index


urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name="index"),
)