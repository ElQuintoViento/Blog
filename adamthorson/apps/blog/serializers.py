# -*- coding: utf-8 -*-
from adamthorson.apps.blog.models import *
from adamthorson.apps.core.serializers import *
from adamthorson.common.serializers import *


class SeriesSerializer(TitleSerializable):
    class Meta:
        model = Series
        fields = ['title']


class SimplePostSerializer(PublishSerializable, SimpleTagSerializable,
                           TimestampSerializable, TitleSerializable):
    series = serializers.CharField(source='series.title')

    class Meta:
        model = Post
        fields = ['created_date', 'modified_date', 'publish_date', 'series',
                  'slug', 'title', 'tags']
        depth = 2


class PostSerializer(PublishSerializable, SimpleTagSerializable,
                     TimestampSerializable, TitleSerializable):
    class Meta:
        model = Post
        fields = ['content', 'created_date', 'modified_date', 'publish_date',
                  'series', 'slug', 'title', 'tags']
        depth = 2
