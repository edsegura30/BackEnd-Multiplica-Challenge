import json

import os
import django
import sys

try:

    sys.path.append('/code/')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
    django.setup()

    from website.models import (
        Event, Reporter, EventType)
except Exception as e:
    print('Unable to setup Django env to parse data')
    print(e)


__DEFAULT_TYPES = [
    'Total', 'Partial', 'Ordinary', 'Extraordinary'
]
__JSON_FILE = '/devutils/api_events_data.json'


def InitEventTypes():
    """Creates the 4 default event types:
      * Total
      * Partial
      * Ordinary
      * Extraordinary
    """
    for event_type in __DEFAULT_TYPES:
        new_event, created = EventType.objects.get_or_create(name=event_type)
        if created:
            new_event.save()


def ParseData():
    """"""
    with open(__JSON_FILE) as json_file:
        data = json.load(json_file)
        events = EventType.objects.all()
        for event in events:
            print(event.name)
        for register in data:
            print(register)
            event_type = EventType.objects.get(name=register['type'])
            reporter, r_created = Reporter.objects.get_or_create(
                name=register['reporter']
            )
            if r_created:
                reporter.save()
            new_event = Event(
                uuid=register['uuid'],
                name=register['name'],
                reporter=reporter,
                event_type=event_type,
                location=register['location'],
                datetime=register['datetime'],
                comment=register['description']
            )
            new_event.save()
            print('Saving event {}'.format(new_event.name))


if __name__ == '__main__':
    InitEventTypes()
    ParseData()
