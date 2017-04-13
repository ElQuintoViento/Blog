# -*- coding: utf-8 -*-
import re
#
from django.core import serializers
from django.shortcuts import get_object_or_404, render
from django.views.generic import View
from django.views.generic.base import RedirectView
#
from adamthorson.apps.blog.models import Post
from adamthorson.apps.blog.serializers import *
from adamthorson.common.helpers import JSONResponse


class ViewPostRedirectView(RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self, slug):
        return slug


# def search_posts(request):
#     # json = Post.objects.values()
#     # return HttpResponse(json, content_type="application/json")
#     JSONSerializer = serializers.get_serializer("json")
#     serializer = JSONSerializer()
#     return serializer.serialize(Post.objects.all())
class SearchPostsView(View):
    def get(self, request, *args, **kwargs):
        data = Post.objects.all()
        serialized_data = PostSerializer(data, many=True).data
        return JSONResponse(serialized_data)


# def view_posts(request):
#    return render(request, 'view_posts.html', {})
class ViewPostsView(View):
    template_name = 'view_posts.html'

    def get(self, request, *args, **kwargs):
        return render(
            request, self.template_name, {})


# def view_post(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     return render(request, 'view_post.html', {'post': post})
class ViewPostView(View):
    template_name = 'view_post.html'

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, 'view_post.html', {'post': post})
