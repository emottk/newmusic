import soundcloud

from django.http import HttpResponse
from django.contrib.auth import login
# from django.contrib.auth.decorators import login_required
from social.apps.django_app.utils import psa
from django.shortcuts import render, redirect
from django.template import loader
from django.conf import settings
from django.views.generic import View
from newmusic.utils.opinions import sort_opinion

# create client object with app credentials
client = soundcloud.Client(
    client_id=settings.SOCIAL_AUTH_SOUNDCLOUD_KEY,
    client_secret=settings.SOCIAL_AUTH_SOUNCLOUD_SECRET,
    redirect_uri='http://localhost:8000/users/register-by-token/soundcloud')

class UserView(View):

    def get(request):
        if request.user.is_authenticated():
            user = request.user
            username = user.get_username()
            sort = sort_opinion(request)
            true_list = sort[0]
            false_list = sort[1]
            return render(request, 'user_page.html', {'username': username, 'true_list': true_list, 'false_list': false_list})
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
