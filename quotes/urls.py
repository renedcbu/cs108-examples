# file: quotes/urls.py

from django.urls import path
from .views import * # HomePageView, QuotePageView, RandomQuotePageView, PersonPageView # our view class definition

urlpatterns = [
    path('', RandomQuotePageView.as_view(), name="random"), # pick a random quote
    path('all', HomePageView.as_view(), name='all'), # generic class-based view
    path('quote/<int:pk>', QuotePageView.as_view(), name='quote'), # show one quote
    path('quote/<int:pk>/update', UpdateQuoteView.as_view(), name='update_quote'), # update a quote
    path('quote/<int:pk>/delete', DeleteQuoteView.as_view(), name='delete_quote'), # update a quote
    path('person/<int:pk>', PersonPageView.as_view(), name='person'), # show one person
    path('person/<int:pk>/add_image', add_image, name='add_image'), # add an image for this person
    path('create_quote', CreateQuoteView.as_view(), name='create_quote'), # create new quotes

]