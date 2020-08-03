from django.test import TestCase

from checkout.forms import OrderForm


class TestOrderForm(TestCase):
    """The following tests the Order Form"""

    def test_name_is_required(self):
        form = OrderForm({
            'full_name': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')

    def test_email_is_required(self):
        form = OrderForm({
            'full_name': 'Tester',
            'email': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_phone_number_is_required(self):
        form = OrderForm({
            'full_name': 'Tester',
            'email': 'test@test.com',
            'phone_number': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.')

    def test_street_address1_is_required(self):
        form = OrderForm({
            'full_name': 'Tester',
            'email': 'test@test.com',
            'phone_number': '123465789',
            'street_address1': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(
            form.errors['street_address1'][0], 'This field is required.')

    def test_town_or_city_is_required(self):
        form = OrderForm({
            'full_name': 'Tester',
            'email': 'test@test.com',
            'phone_number': '123465789',
            'street_address1': '1 Test Avenue',
            'town_or_city': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = OrderForm()
        self.assertEqual(
            form.Meta.fields, (
                'full_name', 'email', 'phone_number',
                'street_address1', 'street_address2',
                'town_or_city', 'postcode', 'county',
                'delivery_option', 'click_and_collect_option',
            ))
