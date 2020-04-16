from django.db import models
from django.urls import * #reverse # to obtain a url from pattern name

# Create your models here.

class Profile(models.Model):
    """Encapsulate the idea of a quote (i.e., text)."""

    # data attribute of a quote
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_adress = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    friends = models.ManyToManyField("self")

    def __str__(self):
        """Return a string representation of this object."""
        return '"%s" - %s - %s - %s ' % (self.first_name, self.last_name, self.city, self.email_adress) 

    def get_status_messages(self):
        status_messages = StatusMessage.objects.filter(profile=self.pk)
        return status_messages
    
    def get_absolute_url(self):
        """Return a URL to display this new quote"""
        return reverse("show_profile_page", kwargs={"pk":self.pk})

    def get_friends(self):
        Myfriends = self.friends.exclude(pk=self.pk)
        return Myfriends

    def get_news_feed(self):
        friends = self.friends.all()
        myself = Profile.objects.filter(pk=self.pk)
        concerned_persons = friends | myself
        news = StatusMessage.objects.filter(profile__in = concerned_persons).order_by("-timestamp")
        return news
    
    def get_friend_suggestions(self):
        friends = self.get_friends()
        myself = Profile.objects.filter(pk=self.pk)
        me_and_myfriends = friends | myself
        friend_suggestions = Profile.objects.exclude(pk__in=me_and_myfriends)
        return friend_suggestions

class StatusMessage(models.Model):
    """Model the data attributes of Facebook status message."""

    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    message = models.TextField(blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    image = models.ImageField(blank=True) # an actual image



    def  __str__(self):
        return '%s %s %s' % (self.timestamp, self.message, self.profile)

