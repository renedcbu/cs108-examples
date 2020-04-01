# file: quotes/urls.py

from django.urls import path
from .views import HomePageView, QuotePageView, RandomQuotePageView # our view class definition

urlpatterns = [
    path('', RandomQuotePageView.as_view(), name="random"), # pick a random quote
    path('all', HomePageView.as_view(), name='home'), # generic class-based view
    path('quote/<int:pk>', QuotePageView.as_view(), name='quote'), # show one quote
]