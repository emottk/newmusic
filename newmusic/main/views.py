
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import View

from newmusic.main.forms import OpinionForm
from newmusic.main.models import Artist
from newmusic.utils.opinions import get_unique_artist



@method_decorator(login_required, name='dispatch')
class ArtistIndex(View):
    template_name = "main/explore.html"

    def get(self, request):
        artist = get_unique_artist(request.user)
        if artist is None:
            return render(request, "main/no_artist.html")
        songs = artist.song_set.all()
        user = request.user
        for song in songs:
            song_url = song.url
        like_form = OpinionForm({'artist': artist.id, 'opinion': True})
        dislike_form = OpinionForm({'artist': artist.id, 'opinion': False})
        return render(request, self.template_name, {
            'artist': artist,
            'song_url': song_url,
            'user': user,
            'like_form': like_form,
            'dislike_form': dislike_form,
        })

    def post(self, request):
        form = OpinionForm(request.POST)
        if form.is_valid():
            opinion = form.save(commit=False)
            opinion.user = request.user
            opinion.save()
        else:
            print(form.errors)
            return HttpResponse("Form is invalid")
        return redirect('explore')


@method_decorator(login_required, name='dispatch')
class OpinionDelete(View):

    def post(self, request, pk):
        opinion = get_object_or_404(request.user.opinion_set, pk=pk)
        opinion.delete()
        if request.is_ajax():
            return HttpResponse(status=204)
        return redirect("user_page", request.user.username)


class AboutIndex(View):
    template_name = "main/about.html"

    def get(self, request):
        return render(request, self.template_name)


class ArtistPage(View):
    template_name = "main/artist_page.html"
    def get(self, request, artist):
        artist_object = get_object_or_404(Artist, name=artist)
        song_url = artist_object.song_set.first().url
        return render(request, self.template_name, {'artist': artist_object, 'song_url': song_url})
