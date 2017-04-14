# -*- coding: utf-8 -*-
from adamthorson.apps.core.models import *
from adamthorson.common.serializers import *


class TagSerializer(NameSerializable):
    class Meta:
        model = Tag
        fields = ['name']


class SimpleTagSerializable(BaseSerializable):
    # tags = TagSerializer(many=True, read_only=True)
    tags = FlatNameField(many=True, read_only=True)

    class Meta:
        abstract = True
