from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase
from sweet_dating_app.forms import EmailUserCreationForm


class FormTestCase(TestCase):
    def test_clean_username(self):
        User.objects.create_user(username='tests-user')

        form = EmailUserCreationForm()
        form.cleaned_data = {'username': 'tests-user2'}

        self.assertEqual(form.clean_username(), 'tests-user2')

    def test_register_sends_email(self):
        form = EmailUserCreationForm()
        form.cleaned_data = {
            'username': 'tests',
            'email': 'tests@tests.com',
            'password1': 'tests-pw',
            'password2': 'tests-pw',
        }
        form.save()
        # Check there is an email to send
        self.assertEqual(len(mail.outbox), 1)
        # Check the subject is what we expect
