# -*- coding: utf-8 -*-
import django_filters
#
from .models import Post


class PostListFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['title']
