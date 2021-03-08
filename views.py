""" Views generate content for the webpages """

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def index(request):
    """ Redirect to the search page, since this is our homepage """
    return HttpResponseRedirect(reverse("database:search"))

def search(request):
    return HttpResponse("Hello world")
