import random
import soundcloud

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from newmusic.main.models import Artist, Song

# create client object with app credentials
client = soundcloud.Client(
    client_id=settings.SOCIAL_AUTH_SOUNDCLOUD_KEY,
    client_secret=settings.SOCIAL_AUTH_SOUNCLOUD_SECRET,
    redirect_uri='http://localhost:8000/users/register-by-token/soundcloud')


def get_artists():
    page_size = 100
    artists_list = []
    url = '/users'
    counter = 0
    max_artists = 200
    while len(artists_list) < max_artists and counter < 20:
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
        url = response.next_href
    artists_list = sorted(artists_list, key=lambda artist: artist["followers_count"])
    return artists_list

def rand(list):
    return random.choice(list)

def get_rand_track_for_artist(artist):
    response = client.get('users/{}/tracks'.format(artist.sc_id))
    track = random.choice(response)
    permalink = track.obj['permalink']
    permalink_url = track.obj['permalink_url']
    return (permalink, permalink_url)

def create_list():
    artist_list = []
    artists = Artist.objects.all()
    for a in artists:
        artist_list.append(a)
    return artist_list

def get_user_avatar(user):
    try:
        sc = user.social_auth.get(provider='soundcloud')
    except ObjectDoesNotExist:
        return None
    return sc.extra_data.get('avatar_url')

def get_user_permalink(user):
    try:
        sc = user.social_auth.get(provider='soundcloud')
    except ObjectDoesNotExist:
        return None
    return sc.extra_data.get('permalink_url')
