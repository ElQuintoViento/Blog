# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
#
from adamthorson.apps.blog.models import Post


def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'view_post.html', {'post': post})
