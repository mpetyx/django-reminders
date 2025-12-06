# django-reminders

[![Build Status](https://img.shields.io/travis/eldarion/django-reminders.svg)](https://travis-ci.org/eldarion/django-reminders)
[![Coverage Status](https://img.shields.io/coveralls/eldarion/django-reminders.svg)](https://coveralls.io/r/eldarion/django-reminders)
[![PyPI](https://img.shields.io/pypi/dm/django-reminders.svg)](https://pypi.python.org/pypi/django-reminders/)
[![PyPI version](https://img.shields.io/pypi/v/django-reminders.svg)](https://pypi.python.org/pypi/django-reminders/)
[![License](https://img.shields.io/badge/license-BSD-blue.svg)](https://pypi.python.org/pypi/django-reminders/)

A user reminder app for site builders to guide users through completion of activities.

## Documentation

Documentation can be found online at [http://django-reminders.readthedocs.org/](http://django-reminders.readthedocs.org/).

## Installation

```bash
pip install django-reminders
```

## Configuration

Add `reminders` to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ...
    "reminders",
    # ...
]
```

Define your reminders in `settings.REMINDERS` (example structure based on usage):

```python
REMINDERS = {
    "my_reminder_label": {
        "dismissable": "session", # or "permanent"
        # ... other config ...
    }
}
```

## Usage

Use the views to handle dismissals.

```python
from django.urls import path
from reminders.views import dismiss

urlpatterns = [
    path("dismiss/<str:label>/", dismiss, name="reminders_dismiss"),
]
```
