from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


class TestUserRegisterForm(TestCase):
	"""The following tests new user creation"""

	def test_username_is_required(self):
		form = UserRegisterForm({'username': ''})
		self.assertFalse(form.is_valid())
		self.assertIn('username', form.errors.keys())
		self.assertEqual(form.errors['username'][0], 'This field is required.')

	def test_email_is_required(self):
		form = UserRegisterForm({'username': 'Test', 'email': ''})
		self.assertFalse(form.is_valid())
		self.assertIn('email', form.errors.keys())
		self.assertEqual(form.errors['email'][0], 'This field is required.')

	def test_email_is_unique(self):
		existing_user = User.objects.create_user('Jimmy', 'jimmy@test.com', 'testing321')

		form = UserRegisterForm({
			'username': 'Test',
			'email': 'jimmy@test.com',
			'password1': 'testing321',
			'password2': 'testing321'
		})
		self.assertFalse(form.is_valid())
		self.assertIn('email', form.errors.keys())
		self.assertEqual(form.errors['email'][0], 'Email address must be unique')


	def test_password_is_required(self):
		form = UserRegisterForm({
			'username': 'Test',
			'email': 'test@test.com',
			'password1': ''
		})
		self.assertFalse(form.is_valid())
		self.assertIn('password1', form.errors.keys())
		self.assertEqual(form.errors['password1'][0], 'This field is required.')

	def test_fields_are_explicit_in_form_metaclass(self):
		form = UserRegisterForm()
		self.assertEqual(form.Meta.fields,
			['username', 'email', 'password1', 'password2'])

	def test_passwords_match(self):
		form = UserRegisterForm({
			'username': 'Test',
			'email': 'test@test.com',
			'password1': 'testing321',
			'password2': 'testing123'
		})
		self.assertFalse(form.is_valid())
		self.assertIn('password2', form.errors.keys())
		self.assertEqual(form.errors['password2'][0],
			'The two password fields didn’t match.')

	def test_profile_created_for_new_user(self):
		user = User.objects.create_user('Jimmy', 'jimmy@test.com', 'testing321')
		profile = Profile.objects.get(pk=user.id)

		self.assertEqual(user.email, profile.user.email)


class TestUserUpdateForm(TestCase):
	"""The following tests profile update functionality"""

	def test_fields_are_explicit_in_form_metaclass(self):
		form = UserUpdateForm()
		self.assertEqual(form.Meta.fields, ['username', 'email'])

	def test_username_and_email_changes_and_saves_to_database(self):
		user = User.objects.create_user('Jimmy', 'jimmy@test.com', 'testing321')

		old_username = user.username
		old_email = user.email
		
		update_user = UserUpdateForm({
			'username': 'Fred',
			'email': 'fred@test.com',
		}, instance=user)
		update_user.save()

		profiles = Profile.objects.all()
		for profile in profiles:
			new_username = profile.user.username
			new_email = profile.user.email
			return [new_username, new_email]

		self.assertNotEquals(old_username, new_username)
		self.assertNotEquals(old_email, new_email)
		self.assertEqual(new_username, 'Fred')
		self.assertEqual(new_email, 'fred@test.com')
		self.assertTrue(
			profiles=Profile.objects.filter(username__exact='Fred')
		)


class TestProfileUpdateForm(TestCase):
	"""The following tests profile update functionality"""

	def test_fields_are_explicit_in_form_metaclass(self):
		form = ProfileUpdateForm()
		self.assertEqual(form.Meta.fields, ['profile_image', 'color_scheme'])

	def test_profile_image_and_colour_scheme_changes_and_saves_to_database(self):
		user = User.objects.create_user('Fred', 'fred@test.com', 'testing321')

		pass
