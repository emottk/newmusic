
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import View

from newmusic.utils.soundcloud import get_artists, rand_artist, get_rand_track_for_artist
from newmusic.main.forms import OpinionForm
from newmusic.main.models import Artist


@method_decorator(login_required, name='dispatch')
class ArtistIndex(View):
    template_name = "main/artist_index.html"

    # def save(self, request):
    #     try:
    #         a = Artist(name=request.POST.get(''))
    #

    def get(self, request):
        try:
            
            rand = rand_artist(artists)
            song_url = get_rand_track_for_artist(rand)
        except ImportError:
            raise Http404("No Artists")
        return render(request, 'main/artist_index.html', {'rand': rand, 'song_url': song_url})

    def post(self, request):
        if request.method == "POST":
            form = OpinionForm({'opinion': False, 'user': request.user})
            import ipdb; ipdb.set_trace()
            if form.is_valid():
                return redirect(request.path)
            else:
                print(form.errors)
                return HttpResponse("Form is invalid")

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
#
# class TemplateView(View)
#     pass
