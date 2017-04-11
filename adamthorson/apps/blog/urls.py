# -*- coding: utf-8 -*-
from django.conf.urls import url
#
from adamthorson.apps.blog.views import *


urlpatterns = [
    url(r'^view/(?P<slug>[^\.]+)$', view_post),
]
