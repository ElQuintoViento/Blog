# -*- coding: utf-8 -*-
from datetime import datetime, timezone
#
from django.contrib.auth.models import User
from django.db import models
#
from adamthorson.common.helpers import datetime_to_epoch_ms

class Contentable(models.Model):
    content = models.TextField(default='<p>None</p>')

    class Meta:
        abstract = True


class Ownable(models.Model):
    owner = models.ForeignKey(User)

    class Meta:
        abstract = True


class Describable(models.Model):
    description = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Permalinkable(models.Model):
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        abstract = True


class Nameable(models.Model):
    name = models.CharField(blank=False, max_length=28)

    class Meta:
        abstract = True


class Publishable(models.Model):
    publish_date = models.DateTimeField(null=True)

    @property
    def publish_date_epoch(self):
        return datetime_to_epoch_ms(self.publish_date)

    class Meta:
        abstract = True


class Timestampable(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    @property
    def created_date_epoch(self):
        return datetime_to_epoch_ms(self.created_date)

    @property
    def modified_date_epoch(self):
        return datetime_to_epoch_ms(self.modified_date)

    class Meta:
        abstract = True


class Titleable(models.Model):
    title = models.CharField(max_length=100, unique=True)

    class Meta:
        abstract = True
