# file: mini_fb/urls.py

from django.urls import path
from .views import * #ShowAllProfilesView, ShowProfilePageView, CreateProfileView

urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='show_profile_page'), # show one person's profile page
    path('profile/<int:profile_pk>/news_feed', ShowNewsFeedView.as_view(), name='show_news_feed'), # show one person's profile page
    path('profile/<int:profile_pk>/add_friend/<int:friend_pk>', add_friend, name='add_friend'), # show one person's profile page
    path('create_profile', CreateProfileView.as_view(), name='create_profile'), # show one person's profile page
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name='update_profile'), # show one person's profile page
    path('profile/<int:pk>/post_status', create_status_message, name='post_status'), # show one person's profile page
    path('profile/<int:pk>/show_possible_friends', ShowPossibleFriendsView.as_view(), name='show_possible_friends'), # show one person's profile page
    path('profile/<int:profile_pk>/delete_status/<int:status_pk>', DeleteStatusMessageView.as_view(), name='delete_status'), # show one person's profile page

]