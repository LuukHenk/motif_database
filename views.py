""" Views generate content for the webpages """

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import models
ProteinDb = models.Proteins

def index(request):
    """ Redirect to the search page, since this is our homepage """
    return HttpResponseRedirect(reverse("database:search"))

def search(request):
    context = {}

    # Process input data if there is a get request
    if request.method == "GET":

        # Check if there is a search query
        search_query = request.GET
        search_filters = {}
        for obj in search_query:
            search_data = search_query[obj].strip()
            if len(search_data) > 0:
                if obj == "motifs":
                    search_filters["{0}__{1}".format(obj, "sequence__icontains")] = search_data
                else:
                    search_filters["{0}__{1}".format(obj, "icontains")] = search_data
                context[obj] = search_data

        # Filter data from the database using the search filters
        context["data_table"] = ProteinDb.objects.filter(**search_filters)

    print(context)

    return render(request, "database/search.html")
