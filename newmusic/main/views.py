
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import View

from newmusic.main.forms import OpinionForm
from newmusic.main.models import Artist
from newmusic.utils.opinions import get_unique_artist



@method_decorator(login_required, name='dispatch')
class ArtistIndex(View):
    template_name = "explore.html"

    def get(self, request):
        """
        pulls unique artist from database, sends artist along with song
        and all important information about both to template
        """
        artist = get_unique_artist(request.user)
        if artist is None:
            return render(request, "no_artist.html")
        user = request.user
        song = artist.song_set.first()
        if song is None:
            return HttpResponse("No Song")
        song_url = song.url
        song_pb_count = song.playback_count
        like_form = OpinionForm({'artist': artist.id, 'opinion': True})
        dislike_form = OpinionForm({'artist': artist.id, 'opinion': False})
        return render(request, self.template_name, {
            'artist': artist,
            'song_url': song_url,
            'song_pb_count': song_pb_count,
            'user': user,
            'like_form': like_form,
            'dislike_form': dislike_form,
        })

    def post(self, request):
        """
        Saves user opinion on artist with hidden form

        """
        form = OpinionForm(request.POST)
        if form.is_valid():
            opinion = form.save(commit=False)
            opinion.user = request.user
            opinion.save()
        else:
            print(form.errors)
            return HttpResponseBadRequest("Form is invalid")
        return redirect('explore')


@method_decorator(login_required, name='dispatch')
class OpinionDelete(View):
    def post(self, request, pk):
        """
        Deletes user opinion on artist with hidden form

        """
        opinion = get_object_or_404(request.user.opinion_set, pk=pk)
        opinion.delete()
        if request.is_ajax():
            return HttpResponse(status=204)
        return redirect("user_page", request.user.username)


class AboutIndex(View):
    template_name = "about.html"

    def get(self, request):
        """
        View for basic about page

        """
        return render(request, self.template_name)


class ArtistPage(View):
    template_name = "artist_page.html"
    def get(self, request, artist):
        """
        Pulls info from artist in database to populate specific artist page,
        as well as song info tied to that artist
        """
        artist_object = get_object_or_404(Artist, name=artist)
        song = artist_object.song_set.first()
        return render(request, self.template_name, {'artist': artist_object, 'song': song})
