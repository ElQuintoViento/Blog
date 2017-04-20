# -*- coding: utf-8 -*-
from datetime import datetime, timezone
#
from django.http import HttpResponse
#
from rest_framework.renderers import JSONRenderer


EPOCH = datetime.utcfromtimestamp(0).replace(tzinfo=timezone.utc)


# class JSONResponse(HttpResponse):
#     def __init__(self, json, **kwargs):
#         super(JSONResponse, self).__init__(
#             json, content_type="application/json", **kwargs)

# An HttpResponse that renders its content into JSON.
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def datetime_to_epoch_ms(dt):
    return int(1000.0 * (dt - EPOCH).total_seconds())
