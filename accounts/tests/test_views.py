from django.test import TestCase, override_settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


@override_settings(
    STATICFILES_STORAGE='django.contrib.staticfiles\
.storage.StaticFilesStorage')
class TestViews(TestCase):
    """The following tests the views"""

    def test_register(self):
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_logout(self):
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/logout.html')

    def test_profile_login_required(self):
        response = self.client.post('/login/?next=/accounts/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
