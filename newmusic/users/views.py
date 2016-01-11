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
    # else:
    # return redirect(client.authorize_url())

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render(request))

def callback(request):
    template = loader.get_template('callback.html')
    return HttpResponse(template.render(request))


# redirect(client.authorize_url())
#
# def home(request):
#     if request.user.is_authenticated():
#         return redirect('done')
#     else redirect client.authorize_url()
# @login_required
# @render_to('home.html')
# def done)
#
#
#
# def logout(request):
#     auth_logout(request)
#     return redirect ('/')

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



# from social.apps.django_app.utils import strategy
# from django.contrib.auth import login
# from django.views.decorators.csrf import csrf_exempt
# # from rest_framework.decorators import api_view, permission_classes
# # from rest_framework import permissions, status
# from django.http import HttpResponse as Response
# @strategy()
# def register_by_access_token(request, backend):
#     user = request.user
#     user = backend.do_auth(
#         access_token=request.DATA.get('access_token'),
#         user=user.is_authenticated() and user or None
#         )
#     if user and user.is_active:
#         return user
#     else:
#         return None
# # @csrf_exempt
# # @api_view(['POST'])
# # @permission_classes((permissions.AllowAny,))
# # def social_register(request):
# #     auth_token = request.DATA.get('access_token', None)
# #     backend = request.DATA.get('backend', None)
# #     if auth_token and backend:
# #         try:
# #             user = auth_by_token(request, backend)
# #         except Exception as err:
# #             return Response(str(err), status=400)
# #         if user:
# #             login(request, user)
# #             return Response("User logged in", status=status.HTTP_200_OK)
# #         else:
# #             return Response("Bad Credentials", status=403)
# #     else:
# #         return Response("Bad request", status=400)
