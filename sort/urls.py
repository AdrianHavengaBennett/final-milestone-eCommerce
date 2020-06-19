from django.urls import path
from .views import sort_low_high, sort_high_low, sort_a_z, sort_z_a

urlpatterns = [
    path('sort-low-high/', sort_low_high, name='sort-low-high'),
	path('sort-high-low/', sort_high_low, name='sort-high-low'),
	path('sort-a-z/', sort_a_z, name='sort-a-z'),
	path('sort-z-a/', sort_z_a, name='sort-z-a'),
]
