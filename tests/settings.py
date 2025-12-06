SECRET_KEY = "fake-key"
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "reminders",
    "tests",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "tests.urls"

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
]

REMINDERS = {
    "test_label_session": {
        "dismissable": "session"
    },
    "test_label_permanent": {
        "dismissable": "permanent"
    },
    "test_label_non_dismissable": {
        "dismissable": "false"
    }
}
