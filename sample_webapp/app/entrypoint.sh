#!/usr/bin/env bash
python manage.py db init
python manage.py db upgrade
python manage.py db migrate
flask run --host=0.0.0.0
