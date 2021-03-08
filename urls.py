""" Urls and the link to the code for this url (views.<name>) """
from django.urls import path

from . import views

app_name = "database"
urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search")
]
