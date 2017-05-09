# -*- coding: utf-8 -*-
from .base import *


DATA_DIR = re.sub(r'(?<=/)[^/]+/+[^/]+/*$', 'data/', BASE_DIR)
LOG_DIR = os.path.join(DATA_DIR, 'log')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '35.185.232.212',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_environment_variable('DATABASE_NAME'),
        'USER': get_environment_variable('DATABASE_USER'),
        'PASSWORD': get_environment_variable('DATABASE_PASSWORD'),
        'HOST': '',
        'PORT': '',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATICFILES_DIRS = ()
