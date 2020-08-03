from django.test import SimpleTestCase
from django.urls import reverse, resolve

from accounts.views import register, logout_user, profile


class TestUrls(SimpleTestCase):
    """The following tests the urls"""

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout_user)

    def test_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)
