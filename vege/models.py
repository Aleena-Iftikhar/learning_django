from django.db import models

# Create your models here.


class recipe(models.Model):
    recipe_name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='Recipes')
