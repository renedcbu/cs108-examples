# File : coogle/urls.py
# Author : Rene de Champs (renedc@bu.edu)

from django.urls import path
from .views import * #ShowAllIngredientsView..

urlpatterns = [

    #HOME
    path('', RandomRecipeView.as_view(), name='home'),

    #INGREDIENTS
    path('all_ingredients', ShowAllIngredientsView.as_view(), name='all_ingredients'),
    path('create_ingredient', CreateIngredientView.as_view(), name='create_ingredient'),
    path('ingredient/<int:pk>', ShowIngredientPageView.as_view(), name='ingredient_page'), 
    path('ingredient/<int:pk>/update', UpdateIngredientView.as_view(), name='update_ingredient'),  
    path('ingredient/<int:ingredient_pk>/delete_ingredient', DeleteIngredientView.as_view(), name='delete_ingredient'), 
    
    #RECIPES
    path('all_recipes', ShowAllRecipesView.as_view(), name='all_recipes'),        
    path('create_recipe', CreateRecipeView.as_view(), name='create_recipe'), 
    path('recipe/<int:pk>', ShowRecipePageView.as_view(), name='recipe_page'), 
    path('recipe/<int:pk>/update', UpdateRecipeView.as_view(), name='update_recipe'),  
    path('recipe/<int:recipe_pk>/delete_recipe', DeleteRecipeView.as_view(), name='delete_recipe'), 
    
    #HARVEST
    path('create_harvest', CreateHarvestView.as_view(), name='create_harvest'), 
    path('harvest/<int:pk>', ShowHarvestPageView.as_view(), name='harvest_page'),
    path('harvest/<int:pk>/update', UpdateHarvestView.as_view(), name='update_harvest'),  
    
    #CALENDAR
    path('calendar', ShowCalendarPageView.as_view(), name='calendar'),
    path('calendar/1', ShowJanuaryMonthPageView.as_view(), name='calendar_1'),
    path('calendar/2', ShowFebruaryMonthPageView.as_view(), name='calendar_2'),
    path('calendar/3', ShowMarchMonthPageView.as_view(), name='calendar_3'),
    path('calendar/4', ShowAprilMonthPageView.as_view(), name='calendar_4'),
    path('calendar/5', ShowMayMonthPageView.as_view(), name='calendar_5'), 
    path('calendar/6', ShowJuneMonthPageView.as_view(), name='calendar_6'),
    path('calendar/7', ShowJulyMonthPageView.as_view(), name='calendar_7'),
    path('calendar/8', ShowAugustMonthPageView.as_view(), name='calendar_8'), 
    path('calendar/9', ShowSeptemberMonthPageView.as_view(), name='calendar_9'), 
    path('calendar/10', ShowOctoberMonthPageView.as_view(), name='calendar_10'), 
    path('calendar/11', ShowNovemberMonthPageView.as_view(), name='calendar_11'),
    path('calendar/12', ShowDecemberMonthPageView.as_view(), name='calendar_12'),
]