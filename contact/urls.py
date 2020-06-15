from django.urls import path
from .views import contact_us, thank_you

urlpatterns = [
    path('', contact_us, name='contact-us'),
    path('thank-you/', thank_you, name='thank-you'),
]