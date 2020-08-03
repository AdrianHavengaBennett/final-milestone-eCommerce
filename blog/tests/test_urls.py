from django.test import SimpleTestCase
from django.urls import reverse, resolve

from blog.views import (
    show_all_posts,
    new_post,
    new_product_post,
    new_show_post,
    get_post_detail,
    edit_post,
    delete_post_request,
    delete_post,
)


class TestUrls(SimpleTestCase):
    """The following tests the urls"""

    def test_show_all_posts_url_resolves(self):
        url = reverse('blog-home')
        self.assertEquals(resolve(url).func, show_all_posts)

    def test_new_post_url_resolves(self):
        url = reverse('new-post')
        self.assertEquals(resolve(url).func, new_post)

    def test_new_product_post_url_resolves(self):
        url = reverse('new-product-post', args=[1])
        self.assertEquals(resolve(url).func, new_product_post)

    def test_new_show_post_url_resolves(self):
        url = reverse('new-show-post', args=[1])
        self.assertEquals(resolve(url).func, new_show_post)

    def test_get_post_detail_url_resolves(self):
        url = reverse('post-detail', args=[1])
        self.assertEquals(resolve(url).func, get_post_detail)

    def test_edit_post_url_resolves(self):
        url = reverse('edit-post', args=[1])
        self.assertEquals(resolve(url).func, edit_post)

    def test_delete_post_request_url_resolves(self):
        url = reverse('delete-request', args=[1])
        self.assertEquals(resolve(url).func, delete_post_request)

    def test_delete_post_url_resolves(self):
        url = reverse('delete-post', args=[1])
        self.assertEquals(resolve(url).func, delete_post)
