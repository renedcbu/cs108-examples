from django.db import models
from django.urls import *

class Ingredient(models.Model):
    """Each ingredients attributes"""

    # data attribute of a quote
    name = models.CharField(max_length=50, blank=False)
    INGREDIENTS_TYPE = (('Vegetable', 'Vegetable'), ('Fruit', 'Fruit'), ('Herb', 'Herb'), ('Meat', 'Meat'), ('Fish', 'Fish'), ('Nut', 'Nut'), ('Fat', 'Fat'), ('Dairy', 'Dairy'), ('Carb', 'Carb'), ('Root', 'Root'),)
    ing_type = models.CharField(max_length = 10, choices=INGREDIENTS_TYPE)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    image = models.ImageField(blank=True)


    def __str__(self):
        """Return a string representation of this object."""
        return '%s - %s' % (self.name, self.ing_type) 



class Recipe(models.Model):
    """Model the data attributes of various Recipes."""

    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    instructions = models.TextField(blank=False)
    ingredients = models.ManyToManyField('Ingredient')
    image_url = models.URLField(blank=True)
    image = models.ImageField(blank=True)

    def  __str__(self):
        return '%s' % (self.name)

    def get_ingredients(self):
        """return list of ingredients"""
        MyIngredients = self.ingredients.all()
        return MyIngredients


class Harvest(models.Model):
    """Model the data attributes of various harvest periods"""
    
    ingredients = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    MONTHS = (('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December'))
    start_month = models.CharField(max_length = 10, choices=MONTHS)
    end_month = models.CharField(max_length = 10, choices=MONTHS)
    comment = models.TextField(blank=True)

    def get_months(self):
        period = dict(Harvest.MONTHS)[self.start_month]
        return period

    def  __str__(self):
        return '%s' % (self.ingredients)