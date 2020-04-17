from django.shortcuts import * #render, redirect
from .models import * #Profile
from django.views.generic import * #ListView, DetailView
from django.views.generic.edit import * #CreateView, UpdateView
from .forms import *
from django.urls import * #reverse

class ShowAllIngredientsView(ListView):
    """Creates a subclass of ListView to display all ingredients."""

    model = Ingredient # retrieve objects of type Ingredient from the database
    template_name = "coogle/all_ingredients.html"
    context_object_name = "all_ingredients" # how to find the data in the template file

class ShowAllRecipesView(ListView):
    """Creates a subclass of ListView to display all recipes."""

    model = Recipe # retrieve objects of type Recipe from the database
    template_name = "coogle/all_recipes.html"
    context_object_name = "all_recipes" # how to find the data in the template file

class ShowIngredientPageView(DetailView):
    """Data for one Ingredient record"""

    model = Ingredient
    template_name = "coogle/ingredient_page.html"
    context_object_name = "ingredient_page"

class ShowRecipePageView(DetailView):
    """Data for one Recipe record"""

    model = Recipe
    template_name = "coogle/recipe_page.html"
    context_object_name = "recipe_page"

class ShowCalendarPageView(ListView):
    """Data for the calendar"""

    model = Harvest
    template_name = "coogle/calendar.html"
    context_object_name = "calendar"
