from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from social.apps.django_app.utils import psa

from newmusic.utils.soundcloud import client, get_user_avatar, get_user_permalink
from newmusic.utils.opinions import sort_true, sort_false


@login_required
def user_root(request, username):
    """
    view for user profile, pulls liked songs from database to populate
    template, as well as a few other pieces of data about user from
    soundcloud profile

    """
    if request.user.username == username:
        true_list = sort_true(request.user)
        false_list = sort_false(request.user)
        avatar_url = get_user_avatar(request.user)
        permalink_url = get_user_permalink(request.user)
        return render(request, 'user_page.html', {
            'username': username,
            'true_list': true_list,
            'false_list': false_list,
            'avatar_url': avatar_url,
            'permalink_url': permalink_url,
            })

    else:
        return HttpResponse("not an active user!")

@psa('social:complete')
def register_by_access_token(request, backend):
    """
    registers user through soundcloud social_auth

    """
    code = request.GET.get('code')
    resource = client.exchange_token(code)
    user = request.backend.do_auth(resource.access_token)
    if user:
        redirect_url = reverse('explore')
        if "next" in request.session:
            redirect_url = request.session.pop("next")
        login(request, user)
        return redirect(redirect_url)
    else:
        return HttpResponse("error")


def login_redirect(request):
    """
    redirects to login page w/ soundcloud

    """
    if "next" in request.GET:
        request.session["next"] = request.GET.get("next")
    return render(request, 'register.html', {"soundcloud_redirect" : client.authorize_url()})

def logout_view(request):
    """
    sends successful logout message to about page
    
    """
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect(reverse('about'))
