# File : coogle/urls.py

from django.urls import path
from .views import * #ShowAllIngredientsView..

urlpatterns = [
    path('', ShowAllIngredientsView.as_view(), name='all_ingredients'),
    path('all_recipes', ShowAllRecipesView.as_view(), name='all_recipes'),
    path('ingredient/<int:pk>', ShowIngredientPageView.as_view(), name='ingredient_page'), # show one ingredient page
    path('recipe/<int:pk>', ShowRecipePageView.as_view(), name='recipe_page'), # show one recipe page
    path('calendar', ShowCalendarPageView.as_view(), name='calendar_page'), # show one recipe page
]