from django.shortcuts import render

from .models import Category
from products.models import Product


def show_categories(request):
    """Renders all categories to categories.html page"""

    categories = Category.objects.all()

    return render(request,
                  'categories/categories.html', {'categories': categories})
