from django.urls import path
from .views import (
	show_all_posts,
	new_post,
	new_product_post,
	new_show_post,
	show_post_detail,
	edit_post,
	delete_post_request,
	delete_post
)

urlpatterns = [
    path('', show_all_posts, name='blog-home'),
    path('new-post/', new_post, name='new-post'),
    path('new-product-post/<int:id>', new_product_post, name='new-product-post'),
    path('new-show-post/<int:id>', new_show_post, name='new-show-post'),
    path('post-detail/<int:id>', show_post_detail, name='post-detail'),
    path('edit-post/<int:id>', edit_post, name='edit-post'),
    path('delete-request/<int:id>', delete_post_request, name='delete-request'),
    path('delete-post/<int:id>', delete_post, name='delete-post'),
]