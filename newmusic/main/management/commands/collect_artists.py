from django.core.management.base import BaseCommand, CommandError
from newmusic.utils.soundcloud import get_artists
from newmusic.main.models import Artist

class Command(BaseCommand):
    help = "Collects artists from Soundcloud API and saves into Database"

    def handle(self, **options):
        artists = get_artists()
        for artist in artists:
            try:
                if Artist.objects.filter(name=artist['permalink']).exists():
                    pass
                else:
                    a = Artist(name=artist['permalink'])
                    a.save()
            except Artist.DoesNotExist:
                raise CommandError('Artist does not exist')

        self.stdout.write(self.style.SUCCESS('Successfully collected artists'))
