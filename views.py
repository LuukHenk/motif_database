""" Views generate content for the webpages """

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def index(request):
    """ Redirect to the search page, since this is our homepage """
    return HttpResponseRedirect(reverse("database:search"))

def search(request):
    return render(request, "database/search.html")
