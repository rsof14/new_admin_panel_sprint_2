#!/usr/bin/env bash
python manage.py makemigrations
python manage.py migrate
python create_superuser.py
