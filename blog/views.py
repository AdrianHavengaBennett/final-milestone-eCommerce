from django.shortcuts import render
from .models import BlogPost


def home(request):
	all_blog_posts = BlogPost.objects.all()

	context = {
		'posts': all_blog_posts
	}

	return render(request, 'blog/index.html', context)
