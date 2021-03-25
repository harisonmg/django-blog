# Django Blog
A simple blog application built with Django.

_Credits:_ [Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)

[![Continuous Integration](https://github.com/harisonmg/django-blog/actions/workflows/ci.yml/badge.svg)](https://github.com/harisonmg/django-blog/actions/workflows/ci.yml)
[![Coverage Status](https://coveralls.io/repos/github/harisonmg/django-blog/badge.svg?branch=master)](https://coveralls.io/github/harisonmg/django-blog?branch=master)

## Required Software
- [Python](https://www.python.org/downloads) 3.6 or greater
- [Pipenv](https://pipenv.pypa.io/en/latest/#install-pipenv-today)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- A modern web browser

## Local Setup
1. Clone the repository
1. Create and activate a virtual environment using `pipenv`
   by running `$ pipenv shell`
1. Install dev dependencies by running `$ pipenv install --dev`
1. Generate compressed static files using `$ python manage.py collectstatic`
1. Run the tests using `$ python manage.py test`
1. Run the database migrations using `$ python manage.py migrate`
1. Create a superuser using `$ python manage.py createsuperuser`
1. Use `$ python manage.py runserver` to run the development server
1. Visit [`localhost:8000`](http://localhost:8000) in your browser
