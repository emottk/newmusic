from django.db import models
from django.conf import settings



class Artist(models.Model):
    name = models.CharField(max_length=100)
    sc_id = models.IntegerField()

    # @classmethod
    # def create(cls, name):
    #     artist = cls(name=name)

class Song(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey('main.Artist', on_delete=models.CASCADE)


class Opinion(models.Model):
    opinion = models.BooleanField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # artist = models.ForeignKey('main.Artist', on_delete=models.CASCADE)
