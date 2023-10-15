from django.db import models

# Create your models here.
# class Food(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return f"{self.name}"
#
# class Image(models.Model):
#     title = models.CharField(max_length=200)
#     image = models.ImageField(upload_to='images')
#     def __str__(self):
#         return self.title

class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Food(models.Model):
    food_name = models.CharField(max_length=255, primary_key=True)
    location = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Ingredient, through='FoodIngredients')

class FoodIngredients(models.Model):
    id = models.AutoField(primary_key=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
