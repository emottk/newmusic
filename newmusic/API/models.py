import soundcloud
from django.conf import settings
from django.db import models



class API(models.Model):
    client = soundcloud.Client(client_id=settings.SOCIAL_AUTH_SOUNDCLOUD_KEY)

    page_size = 100

    tracks = client.get('/tracks', order='playback_count', limit=page_size)
    for track in tracks:
        print(track.title)

# Create your models here.
