# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.
class Event(models.Model):
    """Event data."""
    uuid = models.UUIDField(verbose_name='uuid')
    name = models.CharField(
        max_length=240)
    location = models.CharField(max_length=100,
                                blank=True,
                                )


class Reporter(models.Model):
    """Reporter of events."""
    name = models.CharField(max_length=240)


class EventType(models.Model):
    """Type of Event."""
    name = models.CharField(max_length=100)
