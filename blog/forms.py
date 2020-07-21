from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['title', 'content']

	def __init__(self, *args, **kwargs):
		"""Add placeholders and classes, remove auto-generated
		labels and set autofocus on first field
		"""

		super().__init__(*args, **kwargs)
		placeholders = {
			'title': 'Blog Title',
			'content': 'Content'
		}

		for field in self.fields:
			if field == 'title':
				self.fields['title'].widget.attrs['autofocus'] = True
			
			if self.fields[field].required:
				placeholder = f'{placeholders[field]} *'
			else:
				placeholder = placeholders[field]
			self.fields[field].widget.attrs['placeholder'] = placeholder
			self.fields[field].widget.attrs['class'] = 'stripe-style-input'
			self.fields[field].label = False


class ProductBlogPostForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['product', 'title', 'content']


class ShowBlogPostForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['show', 'title', 'content']
