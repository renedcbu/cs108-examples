from django.shortcuts import render
from .models import * #Profile
from django.views.generic import * #ListView, DetailView
from django.views.generic.edit import * #CreateView, UpdateView
from .forms import *
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.

class ShowAllProfilesView(ListView):
    """Creates a subclass of ListView to display all quotes."""

    model = Profile # retrieve objects of type Profile from the database
    template_name = "mini_fb/show_all_profiles.html"
    context_object_name = "show_all_profiles" # how to find the data in the template file

class ShowProfilePageView(DetailView):
    """Data for one Profile record"""

    model = Profile
    template_name = "mini_fb/show_profile_page.html"
    context_object_name = "show_profile_page"

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateStatusMessageForm()
        context['create_status_form'] = form
        # return this context dictionary
        return context

class CreateProfileView(CreateView):

    form_class = CreateProfileForm
    template_name = "mini_fb/create_profile_form.html"

class UpdateProfileView(UpdateView):
    """A view to update a new quote and save it to the databse."""

    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'
    queryset = Profile.objects.all()

def create_status_message(request, pk):
    '''    Process a form submission to post a new status message.'''
    # find the profile that matches the `pk` in the URL
    profile = Profile.objects.get(pk=pk)

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # read the data from this form submission
        message = request.POST['message']

        # save the new status message object to the database
        if message:

            sm = StatusMessage()
            sm.profile = profile
            sm.message = message
            sm.save()

    # redirect the user to the show_profile_page view
    return redirect(reverse('show_profile_page', kwargs={'pk': pk}))