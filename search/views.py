import operator

from functools import reduce

from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages

from blog.models import BlogPost
from products.models import Product
from faq.models import FAQ
from shows.models import UpcomingShows
from products.views import do_pagination


def blog_search(request):
    """Does a search on all blog posts and sends a searched value
    to the template in order to ascertain whether or not the query set
    has been filtered and also leaves a reminder of what was searched
    """

    searched_input_sequence = request.GET['b-search'].split()
    results = reduce(
        operator.or_, (
            Q(title__icontains=x) |
            Q(author__username__icontains=x) |
            Q(date_created__icontains=x) |
            Q(product__name__icontains=x) |
            Q(show__artist_name__icontains=x) |
            Q(show__venue__location_name__icontains=x)
            for x in searched_input_sequence)
        )

    context = do_pagination(
        request, products=BlogPost.objects.filter(results))

    context['searched_str'] = request.GET['b-search']
    if context['searched_str'] == '':
        messages.error(request, f'Nothing entered into search bar.')
        return redirect('blog-home')

    return render(request, 'blog/blog_home.html', context)


def products_search(request):
    """Does a search on all products and sends a searched value
    to the template in order to ascertain whether or not the query set
    has been filtered and also leaves a reminder of what was searched
    """

    searched_input_sequence = request.GET['p-search'].split()
    results = reduce(
        operator.or_, (
            Q(name__icontains=x) |
            Q(category_name__category_name__icontains=x)
            for x in searched_input_sequence)
        )

    context = do_pagination(
        request, products=Product.objects.filter(results))

    context['searched_str'] = request.GET['p-search']
    if context['searched_str'] == '':
        messages.error(request, f'Nothing entered into search bar.')
        return redirect('products-home')

    return render(request, 'products/index.html', context)


def faqs_search(request):
    """Does a search on all faqs and sends a searched value
    to the template in order to ascertain whether or not the query set
    has been filtered and also leaves a reminder of what was searched
    """

    searched_input_sequence = request.GET['f-search'].split()
    results = reduce(
        operator.or_, (
            Q(question__icontains=x)
            for x in searched_input_sequence))
    faqs = FAQ.objects.filter(results)

    searched_str = request.GET['f-search']
    if searched_str == '':
        messages.error(request, f'Nothing entered into search bar.')
        return redirect('faqs-home')

    context = {
        'faqs': faqs,
        'searched_str': searched_str
    }

    return render(request, 'faq/faq.html', context)


def shows_search(request):
    """Does a search on all shows and sends a searched value
    to the template in order to ascertain whether or not the query set
    has been filtered and also leaves a reminder of what was searched
    """

    searched_input_sequence = request.GET['s-search'].split()
    results = reduce(
        operator.or_, (
            Q(artist_name__icontains=x) |
            Q(venue__location_name__icontains=x) |
            Q(date__icontains=x)
            for x in searched_input_sequence))

    searched_str = request.GET['s-search']
    if searched_str == '':
        messages.error(request, f'Nothing entered into search bar.')
        return redirect('get-shows')

    shows = UpcomingShows.objects.filter(results)

    context = {
        'shows': shows,
        'searched_str': searched_str
    }

    return render(request, 'shows/shows.html', context)
