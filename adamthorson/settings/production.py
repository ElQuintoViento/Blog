# -*- coding: utf-8 -*-
from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATICFILES_DIRS = ()
