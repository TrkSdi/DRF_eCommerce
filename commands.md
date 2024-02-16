# Commands

- Start Project
django-admin startproject name

- Runserver
./manage.py runserver

- Generate Secret Key
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())

pip freeze > requirements.txt

# Packages

Django 
python-dotenv
djangorestframework
pytest
pytest-django
mptt (nested fields)
drf-spectacular (documentation)


## Pytest

pytest -h #print options _and_ config file settings

## Formating

pip install black