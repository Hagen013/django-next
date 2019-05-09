from .base import *

DEBUG=True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(SERVICE_DIR.path('db.sqlite'))
    }
}
