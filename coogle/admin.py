# File : coogle/admin.py
# Author : Rene de Champs (renedc@bu.edu)

from django.contrib import admin
from .models import * #Ingredient, Recipe..

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Harvest)