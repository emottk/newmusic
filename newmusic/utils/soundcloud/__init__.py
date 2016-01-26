import random
import soundcloud

from django.conf import settings
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
        # response2 = client.get('/users/{artist.id}/tracks')
        for resource in response.collection:
            if (
                resource.followers_count >= 200 and
                resource.followers_count <= 5000 and
                resource.track_count > 0
            ):
                artists_list.append({
    				"permalink": resource.permalink,
    				"permalink_url": resource.permalink_url,
    				"followers_count": resource.followers_count,
    				"avatar_url": resource.avatar_url,
                    "id": resource.id,
    			})
            if len(artists_list) == max_artists:
                break
        counter = counter + 1
        url = response.next_href
    artists_list = sorted(artists_list, key=lambda artist: artist["followers_count"])
    return artists_list

def rand(list):
    used_artists = []
    choice = random.choice(list)
    used_artists.append(choice)
    return choice

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

def unique(artist_list):
    ar = artist_list.pop()
    return(ar, artist_list)



        # songs_list.append{}
    # page_size = 100
    # songs_list = []
    # response = client.get('/tracks', limit=page_size)
    # # for artist in artists_list:
    # #     artist_id = artist.id
    # for resource in response:
    #     songs_list.append({
    #         "user_id": resource.user_id,
    #         "title": resource.title,
    #         "permalink": resource.permalink,
    #         "permalink_url": resource.permalink_url,
    #     })
    # return songs_list
