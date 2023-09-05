from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=1000)  
    ingredients = models.TextField()
    cooking_time = models.PositiveIntegerField()
    rating = models.CharField(max_length=4, default='na')

    def __str__(self):
        return self.title