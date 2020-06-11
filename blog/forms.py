from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['title', 'content']


class ProductBlogPostForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['product', 'title', 'content']


# class ShowBlogPostForm(forms.ModelForm):
# 	class Meta:
# 		model = BlogPost
# 		fields = ['show', 'title', 'content']
