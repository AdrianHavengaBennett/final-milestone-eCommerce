from django.test import TestCase, override_settings
from django.urls import reverse


@override_settings(
    STATICFILES_STORAGE='django.contrib.staticfiles\
.storage.StaticFilesStorage')
class TestViews(TestCase):
    """The following tests the views"""

    def test_contact_us_GET(self):
        response = self.client.get(reverse('contact-us'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_thank_you_GET(self):
        response = self.client.get(reverse('thank-you'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/thank_you.html')
