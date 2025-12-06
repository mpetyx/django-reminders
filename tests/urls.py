from django.urls import path
from reminders.views import dismiss

urlpatterns = [
    path('dismiss/<str:label>/', dismiss, name='reminders_dismiss'),
]
