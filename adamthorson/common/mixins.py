# -*- coding: utf-8 -*-
import re
#
from django.apps import apps
from django.db.models import Q
from django.db.models.query import QuerySet


class SearchMixin(QuerySet):
    def search_filter(self, text):
        queryset = self
        queryset = queryset.filter(title__icontains=text)
        #
        if self.model is apps.get_model('blog', 'Post'):
            separated_text = re.findall(r'[a-zA-Z0-9]+', text)
            q = Q()
            for word in separated_text:
                q |= Q(tags__name__iexact=word)
            querset_q = self.filter(q)
            queryset |= querset_q
        return queryset.distinct().order_by('-publish_date')

    class Meta:
        abstract = True
