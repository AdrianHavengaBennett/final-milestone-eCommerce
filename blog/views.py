from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import BlogPost
from .forms import BlogPostForm


def show_all_posts(request):
	"""Renders all of the blog posts to the blog_home.html page"""

	blog_posts = BlogPost.objects.all()

	return render(request, 'blog/blog_home.html', {'posts': blog_posts})


def new_post(request):
	"""Renders new post form and saves new post to our database"""

	if request.method == 'POST':
		form = BlogPostForm(request.POST)
		if form.is_valid():
			temp_form = form.save(commit=False)
			temp_form.author = request.user
			temp_form.save()

			return redirect('blog-home')
	else:
		form = BlogPostForm()

	return render(request, 'blog/new_post.html', {'form': form})


def show_post_detail(request, id):
	"""Renders the post's details"""

	post = BlogPost.objects.get(pk=id)

	return render(request, 'blog/post_detail.html', {'post': post})


def edit_post(request, id):
	"""
	Loads form with contents for editing, and saves data
	to database when complete
	"""

	post = get_object_or_404(BlogPost, pk=id)

	if request.method == "POST":
		form = BlogPostForm(request.POST, instance=post)
		if form.is_valid():
			form.save()
			messages.success(request, f'Post changes saved!')
			return redirect('blog-home')
	else:
		form = BlogPostForm(instance=post)

	context = {
		'form': form,
		'post': post
	}

	return render(request, 'blog/edit_post.html', context)


def delete_post(request):
	pass
