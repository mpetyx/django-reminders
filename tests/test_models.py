from django.test import TestCase
from django.contrib.auth.models import User
from reminders.models import Dismissal

class DismissalModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_dismissal_creation(self):
        dismissal = Dismissal.objects.create(user=self.user, label='test_label')
        self.assertEqual(dismissal.user, self.user)
        self.assertEqual(dismissal.label, 'test_label')
        self.assertIsNotNone(dismissal.dismissed_at)
