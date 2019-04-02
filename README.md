# BackEnd
[![python](https://img.shields.io/badge/python-3.6-blue.svg "python 3.6")](https://docs.python.org/3/whatsnew/3.6.html) [![django-version](https://img.shields.io/badge/django-2.0-blue.svg "Django 2.1.5")](https://docs.djangoproject.com/en/2.1/)
Multiplica second technical challenge.
**Developer:** Edgar Segura
**Date:** April the 1st, 2019

## Features

* Django 2.1 (Don't reinvent the wheel)
* Docker 17.06.0-ce
* Docker-compose
* Ready for AWS S3 static serving (changing a flag and providing key files)
* Models to save data
* Script to save JSON file to the DB (~/code/save_data.py in docker container. I don't think JSON is a great way to save file)
* Postgress
* Ready for deploy to Heroku

## Usage

### First launch
Download the repo to your local machine. Then at the `docker_compose.yml` file level use:
```shell
docker-compose up
```
This will build the image needed, once this process is finished, you need to populate the DB or it will not work. To do this, use the `save_data.py` script inside a container to write to the DB. In another shell session write the next:
```shell
docker-compose run /bin/bash
```
Once inside the container, use the script:
```
python /devutils/save_data.py
```
Be patient, this may take a while depending the size of the file `api_events_data.json`. It takes about 1 minute for 10,000 registers.

### Endpoints usage

#### localhost:8000/events?uuid=<uuid of event>&location=<coordinates>&name=<name>
Will return the lists of all the events. We can filter* by **UUID, name or location**.

#### localhost:8000/events/<uuid>/
Will return the details of a specific event, if not found it will return a 404 Response.

#### localhost:8000/reporters&id=<id of event>&name=<name>
Will return the list of all the reporters. We can filter* by **ID or name** of the reporter.

#### localhost:8000/reporters/events/<id>
Will return the list of events of the specified reported using ID as key. If the reporter is not found, it will return a 404 code.

#### localhost:8000/types?id=<id of type>&name=<name>
Will return the list of all the types availables. We can filter* by **ID or name** of the event type.

#### localhost:8000/types/events/<id>
Will return the list of events of the specified type using ID as key. If the type is not found, it will return a 404 code.

**Notes**
* The filters mentioned are not exclusive and are not case sensitive. You can filter with or without caps letter. The filters also will only look if the parameter specified **contains** that string, will not look for a full match.

Except for the endpoint that returns the detail of a specific event, can be more customized for page size and can be navigated to a specific page using:
* `page_size=<int number>`
* `page=<page_number>`


## Initial Assumptions

* The Event Type is available as a Model instead of a choice value to make it scalable for more event types
* Usage of restframework (Unless specifed, why to reinvent the wheel?)
* "Comment" key refers to "description" real key in the json file.

## Improvement proposal:
* Have the JSON file being passively loades
  * Further improvement will be to not have a JSON file to store things.
  * Instead of using a script, we can provide the JSON file via an endpoint, then trigger the processing of that file using a background task with APS os Celery
