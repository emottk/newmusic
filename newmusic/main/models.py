from django.db import models
from django.conf import settings



class Artist(models.Model):
    name = models.CharField(max_length=100)
    sc_id = models.IntegerField(unique=True)
    url = models.CharField(max_length=100)
    avatar_url = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    artist = models.ForeignKey('main.Artist', on_delete=models.CASCADE)


class Opinion(models.Model):
    opinion = models.BooleanField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    artist = models.ForeignKey('main.Artist', on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "artist")
