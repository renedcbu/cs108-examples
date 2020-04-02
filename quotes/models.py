from django.db import models
from django.urls import reverse # to obtain a url from pattern name
import random

# Create your models here.

class Person(models.Model):
    """Encapsulate the concept of a person, who said some famous quote."""

    name = models.TextField(blank=False)

    def __str__(self):
        """Return a string representation of this person."""
        return self.name

    # get an image at random
    def get_random_image(self):
        """Return an image of this person, chosen at random."""

        # get all images of this person
        images = Image.objects.filter(person=self.pk)

        # then, pick one at random, and return it
        i = random.randint(0, len(images) - 1)
        return images[i]
    
    # get all images for this person
    def get_all_images(self):
        """Return a QuerySet of all images for this person."""

        # get all images of this person
        images = Image.objects.filter(person=self.pk)
        return images

        # get all quotes for this person
    def get_all_quotes(self):
        """Return a QuerySet of all quotes for this person."""

        # get all quotes of this person
        quotes = Quote.objects.filter(person=self.pk)
        return quotes


class Quote(models.Model):
    """Encapsulate the idea of a quote (i.e., text)."""

    # data attribute of a quote
    text = models.TextField(blank=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of this object."""
        return '"%s" - %s' % (self.text, self.person.name) 

    def get_absolute_url(self):
        """Return a URL to display this new quote"""
        return reverse("quote", kwargs={"pk":self.pk})

class Image(models.Model):
    """Represent an image, which is associated with a Person."""

    image_url = models.URLField(blank=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of this image."""
        return self.image_url