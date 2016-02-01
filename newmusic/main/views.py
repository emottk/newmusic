
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import View

from newmusic.main.forms import OpinionForm
from newmusic.main.models import Artist
from newmusic.utils.opinions import get_unique_artist



@method_decorator(login_required, name='dispatch')
class ArtistIndex(View):
    template_name = "main/artist_index.html"

    def get(self, request):
        try:
            artist = get_unique_artist(request.user)
            songs = artist.song_set.all()
            user = request.user
            for song in songs:
                song_url = song.url
        except ImportError:
            raise Http404("No Artists")
        return render(request, 'main/artist_index.html', {'artist': artist, 'song_url': song_url, 'user': user})

    def post(self, request):
        try:
            form = OpinionForm(request.POST)
            if form.is_valid():
                opinion = form.save(commit=False)
                opinion.user = request.user
                opinion.save()
            else:
                print(form.errors)
                return HttpResponse("Form is invalid")
        except ImportError:
            raise Http404("already opinion-ed")
        return redirect('/home')

class AboutIndex(View):
    template_name = "main/about_index.html"

    def get(self, request):
        return render(request, "main/about_index.html")
