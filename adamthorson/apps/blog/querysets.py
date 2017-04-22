# -*- coding: utf-8 -*-
from model_utils.managers import InheritanceQuerySet
#
from adamthorson.common.mixins import *


class PostQuerySet(SearchMixin, InheritanceQuerySet):
    pass
