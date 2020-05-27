from django.shortcuts import render
from .models import BlogPost


def show_all_posts(request):
	"""Renders all of the blog posts to the blog index.html page"""

	all_blog_posts = BlogPost.objects.all()

	context = {
		'posts': all_blog_posts
	}

	return render(request, 'blog/index.html', context)


def new_post(request):
	pass


def show_post_detail(request):
	pass


def edit_post(request):
	pass


def delete_post(request):
	pass
