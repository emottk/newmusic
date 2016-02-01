from django.conf.urls import url, patterns
from . import views
# from django.contrib import admin
# admin.autodiscover()



urlpatterns = patterns('',
    # the view to register our user with a third party token
    # the backend is the python social auth backend e.g. facebook
    url(r'^register-by-token/(?P<backend>[^/]+)/$', views.register_by_access_token),
    url(r'^login$', views.login_redirect, name="login"),
    url(r'^logout$', views.logout_view, name="logout"),
    url(r'^(?P<username>[\w.@+-]+)/$', views.user_root, name="user_page"),
)
