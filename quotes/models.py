from django.db import models

# Create your models here.

class Person(models.Model):
    """Encapsulate the concept of a person, who said some famous quote."""

    name = models.TextField(blank=False)

    def __str__(self):
        """Return a string representation of this person."""
        return self.name

class Quote(models.Model):
    """Encapsulate the idea of a quote (i.e., text)."""

    # data attribute of a quote
    text = models.TextField(blank=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of this object."""
        return '"%s" - %s' % (self.text, self.person.name) 

class Image(models.Model):
    """Represent an image, which is associated with a Person."""

    image_url = models.URLField(blank=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of this image."""
        return self.image_url