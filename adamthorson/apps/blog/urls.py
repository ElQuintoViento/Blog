# -*- coding: utf-8 -*-
from django.conf.urls import url
# from django.views.generic.base import RedirectView
#
from adamthorson.apps.blog.views import *


urlpatterns = [
    # Search posts
    url(r'^$', view_posts),
    url(r'^search/$', search_posts),
    # View posts
    url(r'^(?P<slug>[^\.]+).html$', ViewPostRedirectView.as_view()),
    url(r'^(?P<slug>[^\.]+)$', view_post),
]
