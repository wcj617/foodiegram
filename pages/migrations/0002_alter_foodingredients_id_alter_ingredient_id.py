# Generated by Django 4.2.5 on 2023-10-15 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodingredients',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
