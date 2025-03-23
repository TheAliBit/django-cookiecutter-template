import os
from django.conf import settings  # Use Django settings module to access BASE_DIR

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(settings.BASE_DIR, "static_cdn", "static_root")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(settings.BASE_DIR, "static_cdn", "media_root")

STATICFILES_DIRS = [
    os.path.join(settings.BASE_DIR, "assets")
]