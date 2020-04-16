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

    form = CreateStatusMessageForm(request.POST or None, request.FILES or None)

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # read the data from this form submission
        message = request.POST['message']

        # save the new status message object to the database
        if message or image:

            sm = StatusMessage()
            sm.profile = profile
            sm.message = message
            image = form.save(commit=False)
            image.profile = profile
            image.save()

    # redirect the user to the show_profile_page view
    return redirect(reverse('show_profile_page', kwargs={'pk': pk}))


class DeleteStatusMessageView(DeleteView):
    """A view to update a new quote and save it to the databse."""

    template_name = 'mini_fb/delete_status_form.html'
    queryset = StatusMessage.objects.all()
    #success_url = "../../all" # what to do after deleting a quote

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record for this page view
        context = super(DeleteStatusMessageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        st_msg = StatusMessage.objects.get(pk=self.kwargs['status_pk'])
        context['st_msg'] = st_msg
        # return this context dictionary
        return context
    

    def get_object(self):
        # read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']

        # find the StatusMessage object, and return it
        st_msg = StatusMessage.objects.get(pk=status_pk)
        return st_msg
    
    def get_success_url(self):
        # read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']

        #status = Profile.objects.filter(pk=profile_pk).first()
        #profile = status.profile
        return reverse('show_profile_page', kwargs={'pk':profile_pk})

class ShowNewsFeedView(DetailView):

    model = Profile
    template_name = "mini_fb/show_news_feed.html"
    context_object_name = "show_news_feed"
    queryset = Profile.objects.all()

    def get_object(self):
        # read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']

        # find the StatusMessage object, and return it
        news_feed = Profile.objects.get(pk=profile_pk)
        return news_feed

class ShowPossibleFriendsView(DetailView):
    model = Profile
    template_name =  "mini_fb/show_possible_friends.html"

def add_friend(request, profile_pk, friend_pk):
    og_profile = Profile.objects.get(pk=profile_pk)
    couldbe_friend = Profile.objects.get(pk=friend_pk)
    og_profile.friends.add(couldbe_friend)
    og_profile.save()
    return redirect(reverse("show_profile_page", kwargs={'pk':profile_pk}))