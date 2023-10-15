# Generated by Django 4.2.5 on 2023-10-15 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('food_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FoodIngredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.food')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='ingredients',
            field=models.ManyToManyField(through='pages.FoodIngredients', to='pages.ingredient'),
        ),
    ]