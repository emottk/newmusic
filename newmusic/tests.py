from mock import Mock, patch
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from newmusic.main.models import Artist, Song
from newmusic.main.forms import OpinionForm
from newmusic.utils.populate import collect_artists, collect_songs
from newmusic.utils.soundcloud import get_user_avatar, get_user_permalink
User = get_user_model()

class ArtistPageViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testusername', password='testing')
        self.artist = Artist.objects.create(name="artistname", sc_id=1)

    def test_artist_page_anonymous(self):
        url = reverse('artist_page', args=[self.artist.name])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_artist_page_authed(self):
        self.client.force_login(self.user)
        url = reverse('artist_page', args=[self.artist.name])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class AboutViewTestCase(TestCase):
    def test_about(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)


class UserViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testusername', password='testing')

    def test_user_page_anonymous(self):
        url = reverse('user_page', args=[self.user.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_user_page_authed(self):
        self.client.force_login(self.user)
        url = reverse('user_page', args=[self.user.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_page_inactive_user(self):
        self.client.force_login(self.user)
        url = reverse('user_page', args=['fdafdc'])
        response = self.client.get(url)
        self.assertContains(response, "not an active user!")


class HomeViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testusername', password='testing')

    def test_home_anonymous(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 302)

    def test_home_authed(self):
        self.client.force_login(self.user)
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_view_with_no_artists(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('explore'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'no_artist.html')

    def test_form_submit(self):
        artist = Artist.objects.create(name="artistname", sc_id=1)
        self.client.force_login(self.user)
        response = self.client.post(reverse('explore'), {'artist': artist.id, 'opinion': True})
        self.assertEqual(response.status_code, 302)

    def test_form_submit_invalid_artist(self):
        # artist = Artist.objects.create(name="artistname", sc_id=1)
        self.client.force_login(self.user)
        response = self.client.post(reverse('explore'), {'opinion': True})
        self.assertEqual(response.status_code, 400)

    def test_form_submit_invalid_opinion(self):
        artist = Artist.objects.create(name="artistname", sc_id=1)
        self.client.force_login(self.user)
        response = self.client.post(reverse('explore'), {'artist': artist.id})
        self.assertEqual(response.status_code, 400)


class PopulateTests(TestCase):

    def test_no_song(self):
        """
        tests that we don't save songs that have a value of None
        """
        with patch(
            'newmusic.utils.populate.get_rand_track_for_artist',
            return_value=None
        ):
            collect_songs([{}])
            self.assertEqual(Song.objects.count(), 0)

class FormTests(TestCase):

    def test_form_error(self):
        form_data = {'whatever':'whatever'}
        form = OpinionForm(data=form_data)
        self.assertFalse(form.is_valid())
