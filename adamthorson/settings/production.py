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
    'adamthorson.com',
    'www.adamthorson.com',
    'blog.adamthorson.com',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_environment_variable('DATABASE_NAME'),
        'USER': get_environment_variable('DATABASE_USER'),
        'PASSWORD': get_environment_variable('DATABASE_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATICFILES_DIRS = ()

# Logging configurations
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, "blog.log"),
            'formatter': 'verbose'
        },
        'dbfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, "db.log"),
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
        'django.db.backends': {
            'handlers': ['dbfile'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['file'],
            'propagate': False,
            'level': 'DEBUG',
        }
    }
}
