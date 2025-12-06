from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from reminders.models import Dismissal
from django.urls import path
from reminders.views import dismiss

class DismissViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = Client()
        self.client.login(username='testuser', password='password')
        
    def test_dismiss_session(self):
        response = self.client.post('/dismiss/test_label_session/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.client.session['test_label_session'], 'dismissed')

    def test_dismiss_permanent(self):
        response = self.client.post('/dismiss/test_label_permanent/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Dismissal.objects.filter(user=self.user, label='test_label_permanent').exists())

    def test_dismiss_invalid_method(self):
        response = self.client.get('/dismiss/test_label_session/')
        self.assertEqual(response.status_code, 405)

    def test_dismiss_unknown_label(self):
        response = self.client.post('/dismiss/unknown_label/')
        self.assertEqual(response.status_code, 404)
        
    def test_dismiss_conflict(self):
        response = self.client.post('/dismiss/test_label_non_dismissable/')
        self.assertEqual(response.status_code, 409)
