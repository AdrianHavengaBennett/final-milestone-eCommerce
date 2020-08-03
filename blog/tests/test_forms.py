from django.test import TestCase

from blog.forms import BlogPostForm


class TestBlogPostForm(TestCase):
    """The following tests the BlogPostForm model form"""

    def test_title_is_required(self):
        form = BlogPostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_content_is_required(self):
        form = BlogPostForm({'title': 'Test', 'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')
