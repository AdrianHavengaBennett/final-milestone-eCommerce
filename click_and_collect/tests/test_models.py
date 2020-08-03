from django.test import TestCase

from click_and_collect.models import ClickCollectLocations


class TestClickCollectLocationsModel(TestCase):
    """The following tests the ClickCollectLocations model"""

    def test_location_string_method_returns_location_name(self):
        location = ClickCollectLocations.objects.create(
            location_name='Test Location',
            street_address1='1 Test Ave.',
            street_address2='',
            town_or_city='Testopia',
            postcode='123456',
            location_email='test@test.com',
            location_phone='987654321',
        )

        self.assertEqual(location.__str__(), location.location_name)
