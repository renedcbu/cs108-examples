from django.db import models

# Create your models here.

class Profile(models.Model):
    """Encapsulate the idea of a quote (i.e., text)."""

    # data attribute of a quote
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_adress = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        """Return a string representation of this object."""
        return '"%s" - %s - %s - %s ' % (self.first_name, self.last_name, self.city, self.email_adress) 

    def get_status_messages(self):
        status_messages = StatusMessage.objects.filter(profile=self.pk)
        return status_messages

class StatusMessage(models.Model):
    """Model the data attributes of Facebook status message."""

    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def  __str__(self):
        return '%s %s' % (self.timestamp, self.message)

