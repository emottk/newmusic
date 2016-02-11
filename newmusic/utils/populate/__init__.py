from newmusic.utils.soundcloud import get_artists, get_rand_track_for_artist
from newmusic.main.models import Artist, Song

def collect_artists():
    artists = get_artists()
    for artist in artists:
        if Artist.objects.filter(name=artist['permalink']).exists():
            pass
        else:
            a = Artist(
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
            a.save()

def collect_songs():
    artists = Artist.objects.all()
    for artist in artists:
        song_dic = get_rand_track_for_artist(artist)
        if Song.objects.filter(name=song_dic['permalink']).exists():
            pass
        else:
            s = Song(
                name=song_dic['permalink'],
                url=song_dic['permalink_url'],
                playback_count=song_dic['playback_count'],
                artist_id=artist.id
                )
            s.save()
