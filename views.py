""" Views generate content for the webpages """

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# from . import models
# ProteinDb = models.Proteins

def index(request):
    """ Redirect to the search page, since this is our homepage """
    return HttpResponseRedirect(reverse("database:search"))

def search(request):
    kwargs = {}
    if request.method == "GET":
        search_query = request.GET
        for obj in search_query:
            print(obj)
            # "{0}__{1}".format(obj, "icontains")
    return render(request, "database/search.html")
