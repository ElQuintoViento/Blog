# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.sites.models import Site


def site(request):
    _site = Site.objects.get_current()
    if not settings.PRODUCTION:
        _site = "{}:8000".format(_site)
    return {'site': _site}


def site_prefix(request):
    _site_prefix = "http://"
    if settings.PRODUCTION:
        _site_prefix = "https://"
    return {'site_prefix': _site_prefix}
