from django.urls import path
from .views import show_all_posts, new_post, show_post_detail, edit_post

urlpatterns = [
    path('', show_all_posts, name='blog-home'),
    path('new_post/', new_post, name='new-post'),
    path('post_detail/<int:id>', show_post_detail, name='post-detail'),
    path('edit_post/<int:id>', edit_post, name='edit-post'),
]