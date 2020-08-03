from django.test import TestCase, override_settings
from django.urls import reverse


@override_settings(
    STATICFILES_STORAGE='django.contrib.staticfiles\
.storage.StaticFilesStorage')
class TestViews(TestCase):
    """The following tests the views"""

    def test_get_shows_GET(self):
        response = self.client.get(reverse('get-shows'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shows/shows.html')
