from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class TestModels(TestCase):
	"""The following tests the Profile model"""

	def test_profile_image_default(self):
		user = User.objects.create_user('Jimmy', 'jimmy@test.com', 'testing321')
		profile = Profile.objects.get(pk=user.id)
		self.assertEqual(profile.profile_image.url, '/media/default.jpg')

	def test_profile_colour_scheme_default(self):
		user = User.objects.create_user('Jimmy', 'jimmy@test.com', 'testing321')
		profile = Profile.objects.get(pk=user.id)
		self.assertEqual(profile.color_scheme, 'default-scheme')

	def test_profile_string_method_returns_name(self):
		user = User.objects.create_user('Jimmy', 'jimmy@test.com', 'testing321')
		profile = Profile.objects.get(pk=user.id)
		self.assertEqual(str(profile.user.username), 'Jimmy')
