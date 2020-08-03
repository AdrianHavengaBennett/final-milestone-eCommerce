import os
from os import path

if path.exists('env.py'):
    import env


def get_maps_api_key(request):
    """
    Retrieves the Google Maps API Key env variable
    for use in the base.html page google maps script tag
    """

    g_maps_api_key = os.environ.get('MAPS_API_KEY')

    return {'g_maps_api_key': g_maps_api_key}
