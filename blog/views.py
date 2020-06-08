from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import BlogPost
from .forms import BlogPostForm
from products.models import Product


@login_required
def show_all_posts(request):
	"""Renders all of the blog posts to the blog_home.html page"""

	blog_posts = BlogPost.objects.all()

	return render(request, 'blog/blog_home.html', {'posts': blog_posts})


@login_required
def new_post(request):
	"""Renders new post form and saves post to our database"""

	if request.method == 'POST':
		form = BlogPostForm(request.POST)

		if form.is_valid():
			temp_form = form.save(commit=False)
			temp_form.author = request.user
			temp_form.save()

			return redirect('blog-home')
	else:
		form = BlogPostForm()

	context = {
		'form': form,
	}

	return render(request, 'blog/new_post.html', context)


@login_required
def new_product_post(request, id):
	"""Renders new product post form and saves post to our database"""

	product = Product.objects.get(pk=id)

	if request.method == 'POST':
		form = BlogPostForm(request.POST)

		if form.is_valid():
			temp_form = form.save(commit=False)
			temp_form.author = request.user
			temp_form.save()

			return redirect('blog-home')
	else:
		form = BlogPostForm()

	context = {
		'form': form,
		'product': product
	}

	return render(request, 'blog/new_post.html', context)


@login_required
def show_post_detail(request, id):
	"""Renders the post's details"""

	post = BlogPost.objects.get(pk=id)

	return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def edit_post(request, id):
	"""
	Loads form with contents for editing if user == author, and saves data
	to database when complete.
	"""

	post = get_object_or_404(BlogPost, pk=id)

	if request.user == post.author:
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
	else:
		messages.warning(request, f'Sorry, you do not own this post.')
	
	return render(request, 'blog/post_detail.html', {'post': post})
	


@login_required
def delete_post_request(request, id):
	"""
	Retrieves post if it exists and renders
	delete_confirm.html for delete confirmation
	"""

	post = get_object_or_404(BlogPost, pk=id)

	if request.user == post.author:
		messages.warning(request, f'Are you sure you would like to delete this post?')
		return render(request, 'blog/delete_confirm.html', {'post': post})
	else:
		messages.warning(request, f'Sorry, you do not own this post.')

	return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def delete_post(request, id):
	"""Deletes selected blog post and redirects to blog home"""

	post = get_object_or_404(BlogPost, pk=id)

	post.delete()
	return redirect('blog-home')
