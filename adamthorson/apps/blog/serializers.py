# -*- coding: utf-8 -*-
from adamthorson.apps.blog.models import *
from adamthorson.common.serializers import *


class PostSerializer(BaseSerializable):
    title = serializers.CharField()

    class Meta:
        model = Post
        fields = ['title']
        depth = 1
