from django.db import models
from django.conf import settings



class Artist(models.Model):
    name = models.CharField


class Song(models.Model):
    name = models.CharField
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Opinion(models.Model):
    opinion = models.BooleanField
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
