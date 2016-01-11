from django.http import Http404
from django.shortcuts import render_to_response
from django.views.generic import View
from utils.soundcloud import get_artists


class Index(View):
    template_name = "main/index.html"

    def get(self, request):
        try:
            artists_list = get_artists()
        except ImportError:
            raise Http404("No Artists")
        return render_to_response('main/index.html', {'artists_list': artists_list})
