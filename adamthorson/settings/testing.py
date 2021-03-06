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
