# -*- coding: utf-8 -*-
from django.http import HttpResponse
#
from rest_framework.renderers import JSONRenderer


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
