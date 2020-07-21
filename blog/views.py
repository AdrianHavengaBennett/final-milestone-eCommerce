from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from .models import BlogPost
from .forms import BlogPostForm, ProductBlogPostForm, ShowBlogPostForm
from products.models import Product
from shows.models import UpcomingShows


@login_required
def show_all_posts(request):
	"""Renders all of the blog posts to the blog_home.html page
	with pagination
	"""

	blog_posts = BlogPost.objects.all()
	paginator = Paginator(blog_posts, per_page=8)
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)

	if page.has_next():
		next_url = f'?page={page.next_page_number()}'
	else:
		next_url = ''

	if page.has_previous():
		previous_url = f'?page={page.previous_page_number()}'
	else:
		previous_url = ''

	context = {
		'page': page,
		'next_url': next_url,
		'previous_url': previous_url,
		'on_blog_page': True
	}

	return render(request, 'blog/blog_home.html', context)


@login_required
def new_post(request):
	"""Renders new post form and saves post to our database"""

	if request.method == 'POST':
		form = BlogPostForm(request.POST)

		if form.is_valid():
			temp_form = form.save(commit=False)
			temp_form.author = request.user
			temp_form.save()
			messages.success(request, f'New Blog Post created!')
			return redirect('blog-home')
	else:
		form = BlogPostForm()

	return render(request, 'blog/new_post.html', {'form': form})


@login_required
def new_product_post(request, id):
	"""Renders new product post form and saves post to our database"""

	product = Product.objects.get(pk=id)

	if request.method == 'POST':
		form = ProductBlogPostForm(request.POST, initial={'product': product})

		if form.is_valid():
			temp_form = form.save(commit=False)
			temp_form.author = request.user
			temp_form.save()
			messages.success(request, f'New Blog Post RE: {product} created!')
			return redirect('blog-home')
	else:
		form = ProductBlogPostForm(initial={'product': product})

	context = {
		'form': form,
		'product': product
	}

	return render(request, 'blog/new_post.html', context)


@login_required
def new_show_post(request, id):
	"""Renders new product post form and saves post to our database"""

	show = UpcomingShows.objects.get(pk=id)

	if request.method == 'POST':
		form = ShowBlogPostForm(request.POST, initial={'show': show})

		if form.is_valid():
			temp_form = form.save(commit=False)
			temp_form.author = request.user
			temp_form.save()
			messages.success(request, f'New Blog Post RE: {show} created!')
			return redirect('blog-home')
	else:
		form = ShowBlogPostForm(initial={'show': show})

	context = {
		'form': form,
		'show': show
	}

	return render(request, 'blog/new_post.html', context)


@login_required
def get_post_detail(request, id):
	"""Renders the post's details"""

	post = BlogPost.objects.get(pk=id)

	context = {
		'post': post,
		'on_blog_page': True
	}

	return render(request, 'blog/post_detail.html', context)


@login_required
def edit_post(request, id):
	"""Loads form with contents for editing if user == author, and saves data
	to database when complete.
	"""

	post = get_object_or_404(BlogPost, pk=id)

	if request.user == post.author:
		if request.method == "POST":
			form = BlogPostForm(request.POST, instance=post)
			if form.is_valid():
				form.save()
				messages.success(request, f'Post changes saved!')
				return redirect('post-detail', id=id)
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
	"""Retrieves post if it exists and renders delete_confirm.html 
	for delete confirmation
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

	if request.user == post.author:
		post.delete()
		messages.success(request, f'{post} deleted.')
	else:
		messages.warning(request, f'Sorry, you do not own this post.')
		return render(request, 'blog/post_detail.html', {'post': post})

	return redirect('blog-home')
