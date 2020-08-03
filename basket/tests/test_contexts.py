import datetime
import uuid

from django.test import TestCase
from django.test.client import RequestFactory

from basket.contexts import do_db_query
from products.models import Product
from shows.models import ShowsTickets, UpcomingShows
from click_and_collect.models import ClickCollectLocations
from categories.models import Category


class TestContexts(TestCase):
    """Tests for the database query function"""

    def setUp(self):
        """Sets up a dummy request object to be used"""

        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_correct_model_is_queried_by_database_query_function(self):

        request = self.factory.get('/basket/')

        # A location object is required ...
        location = ClickCollectLocations.objects.create(
            location_name='Test Location',
            street_address1='Testing address 1',
            street_address2='Testing address 2',
            town_or_city='Testopia',
            postcode='TE 5T',
            location_email='test@test.com',
            location_phone='123456789',
        )

        # For a show object, which is required ...
        show = UpcomingShows.objects.create(
            artist_name='The Tester',
            venue=location,
            date=datetime.datetime.now(),
            description='Test Show Description',
        )

        # For a ticket object, which will be queried
        # by the function we're testing
        ticket = ShowsTickets.objects.create(
            custom_id=uuid.uuid4(),
            artist=show,
            ticket_type='Test Ticket',
            price=12.00,
        )

        # A category object is required ...
        category = Category.objects.create(
            category_name='Testing',
        )

        # For a product object, which will be the other
        # object queried by the function we're testing
        product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            category_name=category,
            price=20.00,
        )

        is_this_a_ticket = do_db_query(request, item_id=ticket.custom_id)
        is_this_a_product = do_db_query(request, item_id=product.id)

        self.assertEqual(is_this_a_ticket.artist.artist_name,
                         ticket.artist.artist_name)
        self.assertEqual(is_this_a_product.name, product.name)
        self.assertNotEqual(is_this_a_ticket, is_this_a_product)
