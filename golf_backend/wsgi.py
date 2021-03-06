"""
WSGI config for golf_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""
import sys
path = "/golf_backend"
if path not in sys.path:
    sys.path.append(path)


import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "golf_backend.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
