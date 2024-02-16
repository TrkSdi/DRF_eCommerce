# Commands

- Start Project
django-admin startproject name

- Runserver
./manage.py runserver

- Generate Secret Key
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())

pip freeze > requirements.txt

./manage.py spectacular --file schema.yml  

# Packages

Django 
python-dotenv
djangorestframework
pytest
pytest-django
mptt (nested fields)
drf-spectacular (documentation)
coverage (unit test coverage)


## Pytest

pytest -h #print options _and_ config file settings
pytest -s #display print()
coverage run -m pytest
coverage html (create html report)
factoryboy (create test data)

## Formating

pip install black