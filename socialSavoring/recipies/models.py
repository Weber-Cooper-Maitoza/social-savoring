from django import forms
from django.db import models
from django.contrib import admin
from datetime import datetime
from profiles.models import Profile

# Create your models here.

class Recipe(models.Model):
  
  def __str__(self):
    return self.recipe_name

  creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
  created_timestamp = models.DateTimeField(default=datetime.now, blank=True)
  updated_timestamp = models.DateTimeField(default=datetime.now, blank=True)
  recipe_name = models.CharField(max_length=200)
  recipe_image = models.ImageField(upload_to='recipe_img', default="empty.jpg")
  oven_temp = models.IntegerField(null=True)
  serving_size = models.FloatField()
  recipe_category = models.CharField(max_length=50)
  recipe_tags = models.CharField(max_length=200)
  recipe_instructions = models.TextField()
  # recipe_nutrition = 
  likes = models.IntegerField(default=0)
  

class Ingredient(models.Model):

  def __str__(self):
    return self.ingredient_name

  recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

  ingredient_name = models.CharField(max_length=200)
  ingredient_quanitiy = models.FloatField()
  ingredient_measurement = models.CharField(max_length=200)
  