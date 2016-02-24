import random
import logging
import soundcloud

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from newmusic.main.models import Artist, Song

logger = logging.getLogger(__name__)
# create client object with app credentials
client = soundcloud.Client(
    client_id=settings.SOCIAL_AUTH_SOUNDCLOUD_KEY,
    client_secret=settings.SOCIAL_AUTH_SOUNCLOUD_SECRET,
    redirect_uri='http://localhost:8000/users/register-by-token/soundcloud')


def get_artists():
    """
    Returns artists_list from Soundcloud API

    """
    page_size = 100
    artists_list = []
    url = '/users'
    counter = 0
    max_artists = 200
    while url and len(artists_list) < max_artists:
        logger.warning(
            'retrieving artists, currently have %s, on loop %s',
            len(artists_list), counter)
        response = client.get(url, limit=page_size, linked_partitioning=1)
        for resource in response.collection:
            if (
                resource.followers_count >= 1000 and
                resource.followers_count <= 5000 and
                resource.track_count > 0
            ):
                artists_list.append({
    				"permalink": resource.permalink,
    				"permalink_url": resource.permalink_url,
    				"followers_count": resource.followers_count,
    				"avatar_url": resource.avatar_url,
                    "id": resource.id,
                    "country": resource.country,
                    "city": resource.city,
                    "website": resource.website,
                    "description": resource.description,
    			})
            if len(artists_list) == max_artists:
                break
        counter = counter + 1
        url = getattr(response, 'next_href', None)
    artists_list = sorted(artists_list, key=lambda artist: artist["followers_count"])
    return artists_list

def get_rand_track_for_artist(artist_obj):
    """Returns random track from artist object"""
    response = client.get('users/{}/tracks'.format(artist_obj.sc_id))
    track = random.choice(response)
    artist_id = artist_obj.id
    permalink = track.obj['permalink']
    permalink_url = track.obj['permalink_url']
    playback_count = track.obj['playback_count']
    return ({
        'permalink':permalink,
        'permalink_url':permalink_url,
        'playback_count':playback_count,
        'artist_id':artist_id
        })

def get_user_avatar(user):
    """Returns user avatar"""
    try:
        sc = user.social_auth.get(provider='soundcloud')
    except ObjectDoesNotExist:
        return None
    return sc.extra_data.get('avatar_url')

def get_user_permalink(user):
    """Returns user permalink"""
    try:
        sc = user.social_auth.get(provider='soundcloud')
    except ObjectDoesNotExist:
        return None
    return sc.extra_data.get('permalink_url')
