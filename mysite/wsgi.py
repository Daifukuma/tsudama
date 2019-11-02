"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

#from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

#application = get_wsgi_application()

path = '/home/Tsudama01/tsudama01.pythonanywhere.com/'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('AWS_ACCESS_KEY_ID','<SNIP>')
os.environ.setdefault('AWS_SECRET_ACCESS_KEY','<SNIP>')
os.environ.setdefault('DJANGO_SECRET_KEY','<SNIP>')
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tsudama.settings')
os.environ.setdefault('DJANGO_CONFIGURATION','Prod')

from configurations.wsgi import get_wsgi_application
application = get_wsgi_application()
