# file: mini_fb/urls.py

from django.urls import path
from .views import * #ShowAllProfilesView, ShowProfilePageView, CreateProfileView

urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='show_profile_page'), # show one person's profile page
    path('create_profile', CreateProfileView.as_view(), name='create_profile'), # show one person's profile page

]