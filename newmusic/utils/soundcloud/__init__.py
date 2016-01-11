import soundcloud

from django.conf import settings


# create client object with app credentials
client = soundcloud.Client(client_id=settings.SOCIAL_AUTH_SOUNDCLOUD_KEY,
                           client_secret=settings.SOCIAL_AUTH_SOUNCLOUD_SECRET,
                           redirect_uri='http://localhost:8000/users/register-by-token/soundcloud')


def get_artists():
    page_size = 100
    artists = client.get('/users', limit=page_size)
    artists_list = []
    for resource in artists:
        artists_list.append({
            "permalink": resource.permalink,
            "permalink_url": resource.permalink_url,
            "followers_count": resource.followers_count,
            "avatar_url": resource.avatar_url,
        })
    artists_list = sorted(artists_list, key=lambda artist: artist["followers_count"])
    return artists_list
