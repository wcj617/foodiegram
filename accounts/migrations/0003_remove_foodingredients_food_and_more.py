# Generated by Django 4.2.5 on 2023-10-15 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_food_ingredient_foodingredients_food_ingredients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodingredients',
            name='food',
        ),
        migrations.RemoveField(
            model_name='foodingredients',
            name='ingredient',
        ),
        migrations.DeleteModel(
            name='Food',
        ),
        migrations.DeleteModel(
            name='FoodIngredients',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
    ]
