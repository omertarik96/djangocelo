from django.db import models
from django.contrib.auth.models import User

# Model for each course in the application
# This models consist of Subject, Course and Module


class Subject(models.Model):
    """ This model will implement subject of the courses """
    title = models.CharField(max_length=200) # Title of the subject, max_length 200
    slug = models.SlugField(max_length=200, unique=True) # Slug(url) of the subject, this field wil be unique

    class Meta:
        ordering = ['title'] # Default ordering for the subject model is by title

    def __str__(self):
        """Default return value for this model. This will be used in the admin panel and several different places"""
        return self.title

