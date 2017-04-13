# -*- coding: utf-8 -*-
from django.contrib import admin
#
from adamthorson.apps.blog.models import *


admin.site.register([
    Post, Series
])
