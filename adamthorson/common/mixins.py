# -*- coding: utf-8 -*-
from django.apps import apps
from django.db.models.query import QuerySet


class SearchMixin(QuerySet):
    def search_filter(self, text):
        # if self.model is apps.get_model('blog', 'Post'):
        return self.filter(title__icontains=text)

    class Meta:
        abstract = True
