from django.db import models

# Create your models here.


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    # function to control what showing up or what we get as a result if we need this instance as a string
    def __str__(self):
        return f'{self.title} - {self.slug}'
