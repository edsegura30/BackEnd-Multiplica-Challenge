# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.
class Reporter(models.Model):
    """Reporter of events."""
    name = models.CharField(max_length=240)


class EventType(models.Model):
    """Type of Event."""
    name = models.CharField(max_length=100)


class Event(models.Model):
    """Event data."""
    uuid = models.UUIDField(primary_key=True, verbose_name='uuid', editable=True)
    name = models.CharField(
        max_length=240)
    location = models.CharField(max_length=100)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    datetime = models.CharField(max_length=10)
