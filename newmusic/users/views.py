import soundcloud

from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from social.apps.django_app.utils import psa
from django.shortcuts import render, redirect
from django.template import loader
from django.conf import settings
from django.views.generic import View
from django.utils.decorators import method_decorator
from newmusic.utils.opinions import sort_true, sort_false, unique_list

# create client object with app credentials
client = soundcloud.Client(
    client_id=settings.SOCIAL_AUTH_SOUNDCLOUD_KEY,
    client_secret=settings.SOCIAL_AUTH_SOUNCLOUD_SECRET,
    redirect_uri='http://localhost:8000/users/register-by-token/soundcloud')


@login_required
def user_root(request, username):
    true_list = sort_true(request)
    false_list = sort_false(request)
    return render(request, 'user_page.html', {'username': username, 'true_list': true_list, 'false_list': false_list})

@psa('social:complete')
def register_by_access_token(request, backend):
    print(request.GET)
    code = request.GET.get('code')
    resource = client.exchange_token(code)
    user = request.backend.do_auth(resource.access_token)
    if user:
        redirect_url = reverse('artist_index')
        if "next" in request.session:
            redirect_url = request.session.pop("next")
        login(request, user)
        return redirect(redirect_url)
    else:
        return HttpResponse("error")


def login_redirect(request):
    if "next" in request.GET:
        request.session["next"] = request.GET.get("next")
    return render(request, 'register.html', {"soundcloud_redirect" : client.authorize_url()})

def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect(reverse('about_index'))
