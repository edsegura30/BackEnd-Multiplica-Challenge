# -*- coding: utf-8 -*-
from .models import Event
from .serializers import EventSerializer

from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response


# Create your views here.
class events_list(generics.ListAPIView):
    """Endpoint to list events"""
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()

    def filter_queryset(self, queryset):
        uuid = self.request.query_params.get('uuid', None)
        name = self.request.query_params.get('name', None)
        location = self.request.query_params.get('location', None)
        if uuid and len(uuid) > 0:
            queryset = queryset.filter(uuid__icontains=uuid)
        if name and len(name) > 0:
            queryset = queryset.filter(name__icontains=name)
        if location and len(location) > 0:
            queryset = queryset.filter(location__icontains=location)
        return queryset


class event_detail(generics.RetrieveAPIView):
    """Returns the detail of a single event"""
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()
