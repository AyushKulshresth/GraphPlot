from django.db import models

# Create your models here.
class PrimarySchools(models.Model):
    name = models.CharField(max_length = 40)
    language = models.CharField(max_length = 40)
    category = models.CharField(max_length = 40)
    district = models.CharField(max_length = 40)