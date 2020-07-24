from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from blog.models import BlogPost


class TestBlogPostModel(TestCase):
	"""The following tests the BlogPost model"""

	def test_blog_string_method_returns_title(self):
		user = User.objects.create_user('Jimmy', 'jimmy@test.com', 'testing321')

		post = BlogPost.objects.create(
			author=user,
			title='Test Title',
			content='Test Content',
			date_created=timezone.now(),
		)
		
		self.assertEqual(post.__str__(), post.title)
