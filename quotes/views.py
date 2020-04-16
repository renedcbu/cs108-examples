from django.shortcuts import render

# Create your views here.
from .models import Quote, Person
from django.views.generic import * #ListView, DetailView
from django.views.generic.edit import * #CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import redirect
from .forms import CreateQuoteForm, UpdateQuoteForm, AddImageForm
import random


class HomePageView(ListView):
    """Creates a subclass of ListView to display all quotes."""

    model = Quote # retrieve objects of type Quote from the database
    template_name = "quotes/home.html"
    context_object_name = "all_quotes_list" # how to find the data in the template file

class QuotePageView(DetailView):
    """Show the details for one quote."""
    model = Quote
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'

class RandomQuotePageView(DetailView):
    """Show one quote selected at random."""
    model = Quote
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'

    # pick one quote at random
    def get_object(self):
        """Return a single instance of a Quote object, selected at random."""

        # get all quotes
        all_quotes = Quote.objects.all()

        # pick one at random
        r = random.randint(0, len(all_quotes) -1)
        q = all_quotes[r]
        return q # return this object

class PersonPageView(DetailView):
    """Show all quotes and all images for one person."""

    model = Person
    template_name = "quotes/person.html"
    #context_object_name = "person"

    def get_context_data(self, **kwargs):
        """Return a dictionnary with context data for this template to use."""

        # get the default context data:
        # this will include the Person record for this page view
        context = super(PersonPageView, self).get_context_data(**kwargs)

        # create add image form:
        add_image_form = AddImageForm()
        context['add_image_form'] = add_image_form

        # return the context dictionnary:
        return context


class CreateQuoteView(CreateView):
    """A view to create a new quote and save it to the databse."""

    form_class = CreateQuoteForm
    template_name = 'quotes/create_quote.html'

class UpdateQuoteView(UpdateView):
    """A view to update a new quote and save it to the databse."""

    form_class = UpdateQuoteForm
    template_name = 'quotes/update_quote.html'
    queryset = Quote.objects.all()

class DeleteQuoteView(DeleteView):
    """A view to update a new quote and save it to the databse."""

    template_name = 'quotes/delete_quote.html'
    queryset = Quote.objects.all()
    #success_url = "../../all" # what to do after deleting a quote

    def get_success_url(self):
        """Return the URL to which we should be directed after the delete."""

        # get the pk for this quote
        pk = self.kwargs.get("pk")
        quote = Quote.objects.filter(pk=pk).first() # get one from Queryset

        # find the person associated with the quote
        person = quote.person
        return reverse('person', kwargs={'pk':person.pk})

def add_image(request, pk):
    """A custom view function to handle the submission of an image upload."""

    # find the person for whom we are submitting the image
    person = Person.objects.get(pk=pk)

    # read the request data into AddImageForm object
    form = AddImageForm(request.POST or None, request.FILES or None)
    
    # check if the form is valid, save object to databse
    if form.is_valid():

        image = form.save(commit=False) # create the Image object, but not save
        image.person = person
        image.save() # store to the database

    else:
        print("Error: the form waas not valid.")
    
    # redirect to a new URL, display person page
    url = reverse('person', kwargs={'pk':pk})
    return redirect(url)