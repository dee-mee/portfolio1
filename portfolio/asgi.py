"""
ASGI config for portfolio project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from whitenoise import WhiteNoise
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# This application object is used by any ASGI server configured to use this file.
django_asgi_app = get_asgi_application()

# Define the application for WhiteNoise
application = WhiteNoise(
    django_asgi_app,
    # Root directory for static files
    root=os.path.join(Path(__file__).resolve().parent.parent, 'static'),
    # Prefix for static files
    prefix='/static/',
    # Disable directory listings
    autorefresh=True,
)
