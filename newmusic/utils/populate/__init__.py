from newmusic.utils.soundcloud import get_artists, get_rand_track_for_artist
from newmusic.main.models import Artist, Song

def collect_artists():
    """Calls on soundcloud API to populate database with artists"""
    artists = get_artists()
    for artist in artists:
        if not Artist.objects.filter(name=artist['permalink']).exists():
            if artist.get('description'):
                #truncate description to description max length
                artist['description'] = artist['description'][:Artist._meta.get_field('description').max_length]
            Artist.objects.create(
                name=artist['permalink'],
                sc_id=artist['id'],
                url=artist['permalink_url'],
                avatar_url=artist['avatar_url'],
                country=artist['country'],
                city=artist['city'],
                website=artist['website'],
                description=artist['description'],
                followers_count=artist['followers_count']
                )

def collect_songs(artists=None):
    """Calls on soundcloud API to populate database with songs based on collected artists"""
    artists = artists if artists else Artist.objects.all()
    for artist in artists:
        song_dict = get_rand_track_for_artist(artist)
        if  (
            not Song.objects.filter(artist_id=song_dict['artist_id']).exists() and
            song_dict
        ):
            Song.objects.create(
                name=song_dict['permalink'],
                url=song_dict['permalink_url'],
                playback_count=song_dict['playback_count'],
                artist_id=song_dict['artist_id']
                )
