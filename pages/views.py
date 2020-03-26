# file: pages/views.html
# description: provide a view to send to the user

from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    """A specialized version of TemplateView to display out home page."""

    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    """A specialized version of TemplateView to display out home page."""

    template_name = "pages/about.html"