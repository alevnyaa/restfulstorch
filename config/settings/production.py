from .base import *
from .secret import SECRET_KEY

DEBUG = True

SECRET_KEY = 'fpsuhf8ahfa398pfhawafp389fh3a8hfuofhp9v'

ALLOWED_HOSTS = [
	'govelapp.com',
	'www.govelapp.com',
        '127.0.0.1',
        'localhost',
        '95.85.27.32',
        ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'restfulstorch',
        'USER': 'restfulstorchuser',
        'PASSWORD': 'a123b432',
        'HOST': 'localhost',
        'PORT': '',
    }
}
