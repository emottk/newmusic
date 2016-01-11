from django.conf.urls import include, url, patterns

from main.views import Index


urlpatterns = patterns('',
    url(r'^index/', Index.as_view(), name="index"),
)
