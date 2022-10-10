#!/bin/sh


python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn DRF.wsgi:aplication --bind 0.0.0.0:8000
