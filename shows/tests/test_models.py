import datetime
import uuid

from django.test import TestCase

from click_and_collect.models import ClickCollectLocations
from shows.models import UpcomingShows, ShowsTickets


class TestUpcomingShowsModel(TestCase):
    """The following tests the UpcomingShows model"""

    def test_show_string_method_returns_artist_name_and_venue(self):

        location = ClickCollectLocations.objects.create(
            location_name='Test Location',
            street_address1='Testing address 1',
            street_address2='Testing address 2',
            town_or_city='Testopia',
            postcode='TE 5T',
            location_email='test@test.com',
            location_phone='123456789',
        )
        show = UpcomingShows.objects.create(
            artist_name='Test Artist',
            venue=location,
            date=datetime.datetime.now(),
            description='Test Description',
        )

        self.assertEqual(show.__str__(), f'{show.artist_name} @ {show.venue}')


class TestShowsTicketsModel(TestCase):
    """The following tests the ShowsTickets model"""

    def test_ticket_string_method_returns_artist_name_and_ticket_type(self):

        location = ClickCollectLocations.objects.create(
            location_name='Test Location',
            street_address1='Testing address 1',
            street_address2='Testing address 2',
            town_or_city='Testopia',
            postcode='TE 5T',
            location_email='test@test.com',
            location_phone='123456789',
        )

        show = UpcomingShows.objects.create(
            artist_name='Test Artist',
            venue=location,
            date=datetime.datetime.now(),
            description='Test Description',
        )

        ticket = ShowsTickets.objects.create(
            custom_id=uuid.uuid4(),
            artist=show,
            ticket_type='Test Ticket',
            price=10.00,
        )

        self.assertEqual(
            ticket.__str__(), f'{ticket.artist} | {ticket.ticket_type}')
