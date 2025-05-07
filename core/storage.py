from django.conf import settings
from django.core.files.storage import FileSystemStorage
from whitenoise.storage import CompressedManifestStaticFilesStorage

class CustomMediaStorage(FileSystemStorage):
    """
    Custom file storage for media files that works with WhiteNoise in production.
    """
    def __init__(self, location=None, base_url=None, *args, **kwargs):
        if location is None:
            location = settings.MEDIA_ROOT
        if base_url is None:
            base_url = settings.MEDIA_URL
        super().__init__(location, base_url, *args, **kwargs)

    def url(self, name):
        url = super().url(name)
        # Ensure the URL is absolute
        if url.startswith('http'):
            return url
        return f"{settings.STATIC_URL}{url.lstrip('/')}"
