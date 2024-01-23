from django.db import models

# Create your models here.
class Matches(models.Model):
    season = models.CharField(max_length = 40)
    team1 = models.CharField(max_length = 40)
    team2 = models.CharField(max_length = 40)
    winner = models.CharField(max_length = 40)
