import soundcloud

from django.http import HttpResponse
from django.contrib.auth import login
# from django.contrib.auth.decorators import login_required
from social.apps.django_app.utils import psa
from django.shortcuts import render, redirect
from django.template import loader
from django.conf import settings

# create client object with app credentials
client = soundcloud.Client(
    client_id=settings.SOCIAL_AUTH_SOUNDCLOUD_KEY,
    client_secret=settings.SOCIAL_AUTH_SOUNCLOUD_SECRET,
    redirect_uri='http://localhost:8000/users/register-by-token/soundcloud')


def check(request):
    if request.user.is_authenticated():
        return render(request, 'callback.html')
    else:
        return render(request, 'home.html', {"soundcloud_redirect" : client.authorize_url()})


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render(request))


def callback(request):
    template = loader.get_template('callback.html')
    return HttpResponse(template.render(request))


@psa('social:complete')
def register_by_access_token(request, backend):
    print(request.GET)
    code = request.GET.get('code')
    resource = client.exchange_token(code)
    user = request.backend.do_auth(resource.access_token)
    print(user)
    if user:
        login(request, user)
        return redirect('/users/check')
    else:
        return HttpResponse("error")
