from django.apps import AppConfig


class ArtistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'artist'
# artist/apps.py
from django.apps import AppConfig

class ArtistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'artist'

    def ready(self):
        import artist.signals