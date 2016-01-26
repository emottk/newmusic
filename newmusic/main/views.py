
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import View

from newmusic.utils.soundcloud import rand, create_list, unique
from newmusic.main.forms import OpinionForm
from newmusic.main.models import Artist


@method_decorator(login_required, name='dispatch')
class ArtistIndex(View):
    template_name = "main/artist_index.html"

    def get(self, request):
        try:
            artists = create_list()
            artist, artists = unique(artists)
            songs = artist.song_set.all()
            for song in songs:
                song_url = song.url
        except ImportError:
            raise Http404("No Artists")
        return render(request, 'main/artist_index.html', {'artist': artist, 'song_url': song_url})

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
        return redirect('/')



# class SongIndex(View):
#     template_name = "main/song_index.html"
#
#     def get(self, request):
#         try:
#             artists_list = get_artists()
#             songs_list = get_tracks(artists_list)
#         except ImportError:
#             raise Http404("No Songs")
#         return render(request, 'main/song_index.html', {'songs_list': songs_list})
#
#
# class AboutView(View):
#     template_name = "main/about.html"
