from django.core.management.base import BaseCommand
from newmusic.utils.soundcloud import get_rand_track_for_artist
from newmusic.main.models import Artist, Song

class Command(BaseCommand):
    help = "Collects songs from artists and saves into database"

    def handle(self, **options):
        artists = Artist.objects.all()
        for artist in artists:
            song_dic = get_rand_track_for_artist(artist)
            if Song.objects.filter(name=song_dic['permalink']).exists():
                pass
            else:
                s = Song(
                    name=song_dic['permalink'],
                    url=song_dic['permalink_url'],
                    playback_count=song_dic['playback_count'],
                    artist_id=artist.id
                    )
                s.save()

        self.stdout.write(self.style.SUCCESS('Successfully collected songs'))
