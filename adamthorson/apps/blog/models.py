# -*- coding: utf-8 -*-
from django.db import models
#
from . import managers as BlogManagers
from adamthorson.apps.core.models import *
from adamthorson.common.behaviors import *


class Series(Describable, Titleable, models.Model):
    # Relations
    tags = models.ManyToManyField(Tag, related_name='series', blank=True)
    # Attributes - Mandatory
    # Attributes - Optional
    # Object Manager
    objects = BlogManagers.SeriesManager()
    # Custom Properties
    # Methods
    # Meta and String
    class Meta:
        verbose_name = "Series"
        verbose_name_plural = "Series"
        ordering = ("title",)

    def __str__(self):
        return self.title


class Post(Describable, Ownable, Permalinkable, Publishable, Timestampable,
           Titleable, models.Model):
    # Relations
    series = models.ForeignKey(Series, blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    # Attributes - Mandatory
    content = models.TextField(default='<p>None</p>')
    # Attributes - Optional
    # Object Manager
    objects = BlogManagers.PostManager()
    # Custom Properties
    # Methods
    # Meta and String
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ("owner", "title",)

    def __str__(self):
        return self.title
