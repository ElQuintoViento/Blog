# -*- coding: utf-8 -*-
from django.db import models
#
from . import managers as CoreManagers
from adamthorson.common.behaviors import *


class UserProfile(Ownable, models.Model):
    # Relations
    # Attributes - Mandatory
    # Attributes - Optional
    # Object Manager
    objects = CoreManagers.ProfileManager()
    # Custom Properties
    # Methods
    # Meta and String
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ("owner",)

    def __str__(self):
        return self.owner


class Tag(Nameable, models.Model):
    # Relations
    # Attributes - Mandatory
    # Attributes - Optional
    # Object Manager
    objects = CoreManagers.TagManager()
    # Custom Properties
    # Methods
    # Meta and String
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ("name",)

    def __str__(self):
        return self.name
