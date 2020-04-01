from django.db import models
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