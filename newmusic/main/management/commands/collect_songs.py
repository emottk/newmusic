from django.core.management.base import BaseCommand, CommandError
from newmusic.utils.soundcloud import get_artists, get_rand_track_for_artist
from newmusic.main.models import Artist, Song

class Command(BaseCommand):
    help = "Collects songs from artists and saves into database"

    # def handle(self, **options):
    #     # artists = Artist.objects.all()
    #     # for artist in artists:
    #     #     response = client
    #     artists = Arists.objects.all()
    #     try:
    #         if Artist.objects.filter(name=artist['permalink']).exists():
    #             pass
    #         else:
    #             a = Artist(name=artist['permalink'])
    #             a.save()
    #         except Artist.DoesNotExist:
    #             raise CommandError('Artist does not exist')
    #
    #             self.stdout.write(self.style.SUCCESS('Successfully collected artists'))
    #
    #
    #             def get_rand_track_for_artist(artist):
    #                 response = client.get('users/{}/tracks'.format(artist['id']))
    #                 track = random.choice(response)
    #                 return track.obj['permalink_url']
