from django.db import models

# Create your models here.
class Food(models.Model): 
    name = models.CharField(max_length=100) 
  
    def __str__(self): 
        return f"{self.name}"

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.title