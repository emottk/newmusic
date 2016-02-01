from social.backends.soundcloud import SoundcloudOAuth2 as OriginalOauth

class SoundcloudOAuth2(OriginalOauth):
    EXTRA_DATA = OriginalOauth.EXTRA_DATA + [('avatar_url', 'avatar_url')] + [('permalink_url', 'permalink_url')]
