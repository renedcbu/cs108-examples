from django.shortcuts import render

# Create your views here.
from .models import Profile
from django.views.generic import ListView

class ShowAllProfilesView(ListView):
    """Creates a subclass of ListView to display all quotes."""

    model = Profile # retrieve objects of type Profile from the database
    template_name = "mini_fb/show_all_profiles.html"
    context_object_name = "show_all_profiles" # how to find the data in the template file
    