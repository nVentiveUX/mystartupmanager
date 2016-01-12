"""
WSGI config for mystartupmanager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# TODO: fix setings file to use when WSGI is used.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mystartupmanager.settings")

application = get_wsgi_application()
