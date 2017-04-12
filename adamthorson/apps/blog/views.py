# -*- coding: utf-8 -*-
import re
#
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import RedirectView
#
from adamthorson.apps.blog.models import Post


class ViewPostRedirectView(RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self, slug):
        return slug


def search_posts(request):
    return JsonResponse("[{title: 'junk'}]", safe=False)


def view_posts(request):
    return render(request, 'view_posts.html', {})


def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'view_post.html', {'post': post})
