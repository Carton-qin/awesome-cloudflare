"""WSGI config for formula_recognition project."""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "formula_recognition.settings")
application = get_wsgi_application()
