# BackEnd
Multiplica second technical challenge.
**Developer:** Edgar Segura
**Date:** April the 1st, 2019

## Features

* Django 2.1 (Don't reinvent the wheel)
* Docker
* Docker-compose
* Ready for AWS S3 static serving
* Models to save data
* Script to save JSON file to the DB (~/code/save_data.py in docker container. I don't think JSON is a great way to save file)
* Postgress
* Ready for deploy to Heroku

## Assumptions

* The Event Type is available as a Model instead of a choice value to make it scalable for more event types
* Usage of restframework (Unless specifed, why to reinvent the wheel?)
* "Comment" key refers to "description" real key in the json file.
