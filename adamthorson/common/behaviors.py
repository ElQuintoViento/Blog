# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


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


class Publishable(models.Model):
    publish_date = models.DateTimeField(null=True)

    class Meta:
        abstract = True


class Timestampable(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Titleable(models.Model):
    title = models.CharField(max_length=100, unique=True)

    class Meta:
        abstract = True
