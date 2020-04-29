# File : coogle/views.py
# Author : Rene de Champs (renedc@bu.edu)

from django.shortcuts import * #render, redirect
from .models import * #Ingredient, Recipe..
from django.views.generic import * #ListView, DetailView..
from django.views.generic.edit import * #CreateView, UpdateView..
from .forms import *
from django.urls import * #reverse

class HomePageView(TemplateView):
    """A specialized version of TemplateView to display out home page."""

    template_name = "coogle/home.html"

class ShowAllIngredientsView(ListView):
    """Creates a subclass of ListView to display all ingredients."""

    model = Ingredient # retrieve objects of type Ingredient from the database
    template_name = "coogle/all_ingredients.html" # template name
    context_object_name = "all_ingredients" # how to find the data in the template file

class ShowAllRecipesView(ListView):
    """Creates a subclass of ListView to display all recipes."""

    model = Recipe 
    template_name = "coogle/all_recipes.html"
    context_object_name = "all_recipes"

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

class ShowHarvestPageView(DetailView):
    """Data for one Harvest record"""

    model = Harvest
    template_name = "coogle/harvest_page.html"
    context_object_name = "harvest_page"

class ShowCalendarPageView(ListView):
    """Data for the calendar"""

    model = Harvest
    template_name = "coogle/calendar.html"
    context_object_name = "calendar"

class ShowJanuaryMonthPageView(ListView):
    """Data for a month of the calendar"""

    model = Harvest
    template_name = "coogle/calendar_1.html"
    context_object_name = "calendar_month"

class ShowFebruaryMonthPageView(ListView):
    """Data for a month of the calendar"""

    model = Harvest
    template_name = "coogle/calendar_2.html"
    context_object_name = "calendar_month"

class ShowMarchMonthPageView(ListView):
    """Data for a month of the calendar"""

    model = Harvest
    template_name = "coogle/calendar_3.html"
    context_object_name = "calendar_month"

class ShowAprilMonthPageView(ListView):
    """Data for a month of the calendar"""

    model = Harvest
    template_name = "coogle/calendar_4.html"
    context_object_name = "calendar_month"

class ShowMayMonthPageView(ListView):
    """Data for a month of the calendar"""

    model = Harvest
    template_name = "coogle/calendar_5.html"
    context_object_name = "calendar_month"

class ShowJuneMonthPageView(ListView):
    """Data for a month of the calendar"""

    model = Harvest
    template_name = "coogle/calendar_6.html"
    context_object_name = "calendar_month"

class ShowJulyMonthPageView(ListView):
    """Data for a month of the calendar"""

    model = Harvest
    template_name = "coogle/calendar_7.html"
    context_object_name = "calendar_month"

class ShowAugustMonthPageView(ListView):
    """Data for a month of the calendar"""

    model = Harvest
    template_name = "coogle/calendar_8.html"
    context_object_name = "calendar_month"

class ShowSeptemberMonthPageView(ListView):
    """Data for a month of the calendar"""

    model = Harvest
    template_name = "coogle/calendar_9.html"
    context_object_name = "calendar_month"

class ShowOctoberMonthPageView(ListView):
    """Data for a month of the calendar"""

    model = Harvest
    template_name = "coogle/calendar_10.html"
    context_object_name = "calendar_month"

class ShowNovemberMonthPageView(ListView):
    """Data for a month of the calendar"""

    model = Harvest
    template_name = "coogle/calendar_11.html"
    context_object_name = "calendar_month"

class ShowDecemberMonthPageView(ListView):
    """Data for a month of the calendar"""

    model = Harvest
    template_name = "coogle/calendar_12.html"
    context_object_name = "calendar_month"

class CreateIngredientView(CreateView):
    """CreateView that links url to create form"""

    form_class = CreateIngredientForm
    template_name = "coogle/create_ingredient_form.html"

class CreateRecipeView(CreateView):
    """CreateView that links url to create form"""

    form_class = CreateRecipeForm
    template_name = "coogle/create_recipe_form.html"

class CreateHarvestView(CreateView):
    """CreateView that links url to create form"""

    form_class = CreateHarvestForm
    template_name = "coogle/create_harvest_form.html"

class UpdateIngredientView(UpdateView):
    """UpdateView that links url to update form"""

    form_class = UpdateIngredientForm
    template_name = 'coogle/update_ingredient_form.html'
    queryset = Ingredient.objects.all()

    def get_success_url(self):
        ingredient_pk = self.kwargs['pk']
        return reverse('ingredient_page', kwargs={'pk':ingredient_pk})

class UpdateRecipeView(UpdateView):
    """UpdateView that links url to update form"""

    form_class = UpdateRecipeForm
    template_name = 'coogle/update_recipe_form.html'
    queryset = Recipe.objects.all()

    def get_success_url(self):
        recipe_pk = self.kwargs['pk']
        return reverse('recipe_page', kwargs={'pk':recipe_pk})

class UpdateHarvestView(UpdateView):
    """UpdateView that links url to update form"""

    form_class = UpdateHarvestForm
    template_name = 'coogle/update_harvest_form.html'
    queryset = Harvest.objects.all()

    def get_success_url(self):
        ingredient_pk = self.kwargs['pk']
        return reverse('harvest_page', kwargs={'pk':ingredient_pk})

class DeleteIngredientView(DeleteView):
    """A view to delete an ingredient page."""
    
    template_name = 'coogle/delete_ingredient.html'
    queryset = Ingredient.objects.all()

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''
        context = super(DeleteIngredientView, self).get_context_data(**kwargs)
        ingredi = Ingredient.objects.get(pk=self.kwargs['ingredient_pk'])
        context['ingredi'] = ingredi
        return context
    
    def get_object(self):
        ingredient_pk = self.kwargs['ingredient_pk']
        ingredi = Ingredient.objects.get(pk=ingredient_pk)
        return ingredi
    
    def get_success_url(self):
        return reverse('all_ingredients')

class DeleteRecipeView(DeleteView):
    """A view to delete a recipe page."""

    template_name = 'coogle/delete_recipe.html'
    queryset = Recipe.objects.all()

    def get_context_data(self, **kwargs):
        context = super(DeleteRecipeView, self).get_context_data(**kwargs)
        recp = Recipe.objects.get(pk=self.kwargs['recipe_pk'])
        context['recp'] = recp
        return context
    
    def get_object(self):
        recipe_pk = self.kwargs['recipe_pk']
        recp = Recipe.objects.get(pk=recipe_pk)
        return recp
    
    def get_success_url(self):
        return reverse('all_recipes')

class RandomRecipeView(DetailView):
    """Show one recipe selected at random."""
    model = Recipe
    template_name = 'coogle/home.html'
    context_object_name = 'random_recipe'

    def get_object(self):
        """Return a single instance of a Recipe object, selected at random."""
        all_recipes = Recipe.objects.all()
        r = random.randrange(0, abs(len(all_recipes)))
        q = all_recipes[r]
        return q 