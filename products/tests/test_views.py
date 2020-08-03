from django.test import TestCase, override_settings
from django.urls import reverse


@override_settings(
    STATICFILES_STORAGE='django.contrib.staticfiles\
.storage.StaticFilesStorage')
class TestViews(TestCase):
    """The following tests the views"""

    def test_show_products_GET(self):
        response = self.client.get(reverse('products-home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/index.html')
