# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class ToDo(models.Model):
    name = models.CharField(max_length=75, unique=True)
    slug = models.SlugField()
    assigned = models.ForeignKey(User, related_name='AssignedUser', null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=75, choices=settings.TODO_STATUSES, default='new')

    def __str__(self):
        return self.name
