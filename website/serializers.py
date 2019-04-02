from rest_framework import serializers

from .models import Event, EventType, Reporter


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = (
            'id', 'name',)


class ReporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporter
        fields = (
            'id', 'name')


class EventSerializer(serializers.ModelSerializer):
    event_type = EventTypeSerializer()
    reporter = ReporterSerializer()

    class Meta:
        model = Event
        fields = (
            'uuid', 'comment', 'datetime', 'event_type',
            'location', 'name', 'reporter',)
