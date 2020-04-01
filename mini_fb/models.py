from django.db import models

# Create your models here.
# added comment

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
