from django.db import models

# Create your models here.


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    gender     = models.CharField(max_length=1)

    class Meta:
        db_table = 'tbl_actor'