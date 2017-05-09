# -*- coding: utf-8 -*-
from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

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
