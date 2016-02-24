from django.core.management.base import BaseCommand
from newmusic.utils.populate import collect_artists, collect_songs

class Command(BaseCommand):
    help = "Collects Artists and Songs from Soundcloud API and saves into database"

    def handle(self, **options):
        collect_artists()
        collect_songs()

        self.stdout.write(self.style.SUCCESS('Successfully saved artists and songs'))
