from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.email


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

class Food(models.Model):
    food_name = models.CharField(max_length=255, primary_key=True)
    location = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Ingredient, through='FoodIngredients')

class FoodIngredients(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
