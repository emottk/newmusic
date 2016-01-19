from django.core.management.base import BaseCommand, CommandError
from newmusic.utils.soundcloud import get_rand_track_for_artist
from newmusic.main.models import Artist, Song

class Command(BaseCommand):
    help = "Collects songs from artists and saves into database"

    def handle(self, **options):
        # artists = Artist.objects.all()
        # for artist in artists:
        #     response = client
        artists = Artist.objects.all()
        for artist in artists:
            song = get_rand_track_for_artist(artist)
            try:
                if Song.objects.filter(name=song[0]).exists():
                    pass
                else:
                    s = Song(name=song[0], url=song[1], artist_id=artist.id)
                    s.save()
            except Song.DoesNotExist:
                raise CommandError('Song does not exist')

        self.stdout.write(self.style.SUCCESS('Successfully collected songs'))
