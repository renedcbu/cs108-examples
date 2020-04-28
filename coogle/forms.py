# File : coogle/forms.py
# Author : Rene de Champs (renedc@bu.edu)

from django import *
from .models import * #Ingredient, Recipe..

class CreateIngredientForm(forms.ModelForm):
    """A form to add an ingredient to the database"""

    name = forms.CharField(label="Name", max_length=50, required=True)
    INGREDIENTS_TYPE = (('Vegetable', 'Vegetable'), ('Fruit', 'Fruit'), ('Herb', 'Herb'), ('Meat', 'Meat'), ('Fish', 'Fish'), ('Nut', 'Nut'), ('Fat', 'Fat'), ('Dairy', 'Dairy'), ('Carb', 'Carb'), ('Root', 'Root'),)
    ing_type = forms.CharField(label="Type", max_length = 10, widget=forms.Select(choices= INGREDIENTS_TYPE))
    description = forms.CharField(label="Description", required=False)
    image_url = forms.URLField(label="Image URL", required=False)

    class Meta:
        """Associate this form with the Ingredient model."""
        model = Ingredient
        fields = ['name', 'ing_type', 'description', 'image_url']

class CreateRecipeForm(forms.ModelForm):
    """A form to add a recipe to the database"""

    class Meta:
        """Associate this form with the Recipe model."""
        model = Recipe
        fields = ['name', 'description', 'instructions', 'ingredients', 'image_url']

class CreateHarvestForm(forms.ModelForm):
    """A form to add harvest data of an ingredient to the database"""

    class Meta:
        """Associate this form with the Harvest model."""
        model = Harvest
        fields = ['ingredients', 'start_month', 'end_month', 'comment',]

class UpdateIngredientForm(forms.ModelForm):
    """A form to update an ingredient data"""

    class Meta:
        """Associate this form with the Ingredient model."""
        model = Ingredient
        fields = {'name', 'ing_type', 'description', 'image_url'}

class UpdateRecipeForm(forms.ModelForm):
    """A form to update a recipe data"""

    class Meta:
        """Associate this form with the Recipe model."""
        model = Recipe
        fields = {'name', 'description', 'instructions', 'ingredients', 'image_url'}

class UpdateHarvestForm(forms.ModelForm):
    """A form to update an ingredient harvest data"""

    class Meta:
        """Associate this form with the Harvest model."""
        model = Harvest
        fields = {'ingredients', 'start_month', 'end_month', 'comment'}
