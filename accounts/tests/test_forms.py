from django.test import TestCase
from django.contrib.auth.models import User

from accounts.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from accounts.models import Profile


class TestUserRegisterForm(TestCase):
    """The following tests new user creation"""

    def test_username_is_required(self):
        form = UserRegisterForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'][0], 'This field is required.')

    def test_first_name_is_required(self):
        form = UserRegisterForm({
            'username': 'Test',
            'first_name': '',
            'last_name': 'tester',
            'email': 'test@test.com'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(
            form.errors['first_name'][0], 'This field is required.')

    def test_last_name_is_required(self):
        form = UserRegisterForm({
            'username': 'Test',
            'first_name': 'test',
            'last_name': '',
            'email': 'test@test.com'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())
        self.assertEqual(
            form.errors['last_name'][0], 'This field is required.')

    def test_email_is_required(self):
        form = UserRegisterForm({
            'username': 'Test',
            'email': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_email_is_unique(self):
        existing_user = User.objects.create_user(
            'Jimmy', 'jimmy@test.com', 'testing321'
        )

        form = UserRegisterForm({
            'username': 'Test',
            'email': 'jimmy@test.com',
            'password1': 'testing321',
            'password2': 'testing321'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(
            form.errors['email'][0], 'Email address must be unique')

    def test_password_is_required(self):
        form = UserRegisterForm({
            'username': 'Test',
            'email': 'test@test.com',
            'password1': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('password1', form.errors.keys())
        self.assertEqual(
            form.errors['password1'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = UserRegisterForm()
        self.assertEqual(
            form.Meta.fields, ['username', 'first_name', 'last_name',
                               'email', 'password1', 'password2'])

    def test_passwords_match(self):
        form = UserRegisterForm({
            'username': 'Test',
            'email': 'test@test.com',
            'password1': 'testing321',
            'password2': 'testing123'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors.keys())
        self.assertEqual(
            form.errors['password2'][0],
            'The two password fields didn’t match.')

    def test_profile_created_for_new_user(self):
        user = User.objects.create_user(
            username='Jimmy',
            first_name='Jim',
            last_name='Test',
            email='jimmy@test.com',
            password='testing321'
        )
        profile = Profile.objects.get(pk=user.id)

        self.assertEqual(user.email, profile.user.email)


class TestUserUpdateForm(TestCase):
    """The following tests user update functionality"""

    def test_fields_are_explicit_in_form_metaclass(self):
        form = UserUpdateForm()
        self.assertEqual(
            form.Meta.fields, ['username', 'first_name',
                               'last_name', 'email'])

    def test_user_details_change_and_save_to_database(self):
        user = User.objects.create_user(
            username='Jimmy',
            first_name='Jim',
            last_name='Test',
            email='jimmy@test.com',
            password='testing321'
        )

        old_username = user.username
        old_first_name = user.first_name
        old_last_name = user.last_name
        old_email = user.email

        update_user = UserUpdateForm({
            'username': 'Fred',
            'first_name': 'Fred',
            'last_name': 'Testing',
            'email': 'fred@test.com',
        }, instance=user)
        update_user.save()

        user = User.objects.get(pk=user.id)

        new_username = user.username
        new_first_name = user.first_name
        new_last_name = user.last_name
        new_email = user.email

        self.assertNotEquals(old_username, new_username)
        self.assertNotEquals(old_first_name, new_first_name)
        self.assertNotEquals(old_last_name, new_last_name)
        self.assertNotEquals(old_email, new_email)
        self.assertEqual(new_username, user.username)
        self.assertEqual(new_first_name, user.first_name)
        self.assertEqual(new_last_name, user.last_name)
        self.assertEqual(new_email, user.email)


class TestProfileUpdateForm(TestCase):
    """The following tests profile update functionality"""

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ProfileUpdateForm()
        self.assertEqual(form.Meta.fields, ['profile_image', 'color_scheme'])

    def test_colour_scheme_changes_and_saves_to_database(self):
        user = User.objects.create_user(
            username='Jimmy',
            first_name='Jim',
            last_name='Test',
            email='jimmy@test.com',
            password='testing321'
        )

        profile = User.objects.get(pk=user.id)

        # Checks that the profile color scheme is default
        self.assertEqual(user.profile.color_scheme, 'default-scheme')

        # Then we change the scheme
        update_scheme_form = ProfileUpdateForm({
            'color_scheme': 'red-scheme'}, instance=user.profile)
        update_scheme_form.save()

        # And run the checks once more
        self.assertEqual(user.profile.color_scheme, 'red-scheme')
