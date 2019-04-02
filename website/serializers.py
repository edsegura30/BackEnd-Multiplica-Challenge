from rest_framework import serializers

from .models import Event, EventType, Reporter


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = (
            'id', 'name',)


class EventSerializer(serializers.ModelSerializer):
    event_type = EventTypeSerializer()

    class Meta:
        model = Event
        fields = (
            'uuid', 'name', 'event_type', 'location', 'comment', 'datetime')
