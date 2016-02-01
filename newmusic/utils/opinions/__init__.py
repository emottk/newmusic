from django.conf import settings
from django.contrib.auth.models import User
from newmusic.main.models import Artist, Opinion
from newmusic.utils.soundcloud import rand

def sort_true(user):
    true_list = user.opinion_set.filter(opinion=True)
    return true_list

def sort_false(user):
    false_list = user.opinion_set.filter(opinion=False)
    return false_list

def get_unique_artist(user):
    """
    Return a random artist that a user has no opinion on

    """
    seen_ids = user.opinion_set.values_list("artist_id", flat=True)
    return Artist.objects.exclude(id__in=seen_ids).order_by('?').first()
