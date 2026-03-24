from django.db import models

# Create your models here.

class std(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.TextField()

class car(models.Model):
    name = models.CharField()
    speed = models.IntegerField()

    def __str__(self):        # read a specific attribute
        return self.name