# File : coogle/models.py
# Author : Rene de Champs (renedc@bu.edu)

from django.db import models
from django.urls import *
import random

class Ingredient(models.Model):
    """Each ingredients attributes"""

    name = models.CharField(max_length=50, blank=False)
    INGREDIENTS_TYPE = (('Vegetable', 'Vegetable'), ('Fruit', 'Fruit'), ('Herb', 'Herb'), ('Meat', 'Meat'), ('Fish', 'Fish'), ('Nut', 'Nut'), ('Fat', 'Fat'), ('Dairy', 'Dairy'), ('Carb', 'Carb'), ('Root', 'Root'),)
    ing_type = models.CharField(max_length = 10, choices=INGREDIENTS_TYPE)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        """Return a string representation of this object."""
        return '%s' % (self.name) 

    def get_ingredient(self):
        """Return ingredient"""
        me = Ingredient.objects.filter(pk=self.pk)
        return me

    def get_absolute_url(self):
        """Return a URL to display this new ingredient"""
        return reverse("ingredient_page", kwargs={"pk":self.pk})

    def get_recipes(self):
        """Finds recipes related to an ingredient"""
        recipes = Recipe.objects.filter(ingredients=self.pk)
        return recipes
    

class Recipe(models.Model):
    """Model the data attributes of various Recipes."""

    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=500, blank=True)
    instructions = models.TextField(blank=False)
    ingredients = models.ManyToManyField('Ingredient')
    image_url = models.URLField(blank=True)

    def  __str__(self):
        """Return a string representation of this object."""
        return '%s' % (self.name)

    def get_ingredients(self):
        """return list of ingredients"""
        MyIngredients = self.ingredients.all()
        return MyIngredients

    def get_random_recipe(self):
        """Return a recipe, chosen at random."""
        recipes = Recipe.objects.all()
        i = random.randint(0, len(recipes) - 1)
        return recipes[i]


class Harvest(models.Model):
    """Model the data attributes of various harvest periods"""
    
    ingredients = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    MONTHS = (('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December'))
    start_month = models.CharField(max_length = 10, choices=MONTHS)
    end_month = models.CharField(max_length = 10, choices=MONTHS)
    comment = models.TextField(blank=True)

    def  __str__(self):
        """Return a string representation of this object."""
        return '%s' % (self.ingredients)