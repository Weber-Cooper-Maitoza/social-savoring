from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe, Ingredient
from profiles.models import Profile
from django.contrib.auth.models import User
from datetime import datetime
import os
import re

# Create your views here.

@login_required
def recipe_list_view(request, id):
  profile = Profile.objects.get(user=User.objects.get(id=id))
  recipes = Recipe.objects.filter(creator=profile)
  return render(request, 'recipes/my_recipes.html', {'recipes': recipes, 'profile': profile})


@login_required
def recipe_detail_view(request, id):
  # profile = Profile.objects.get(user=User.objects.get(id=id))
  recipe = Recipe.objects.get(pk=id)
  profile = recipe.creator
  ingredient_list = Ingredient.objects.filter(recipe=recipe.id)
  return render(request, 'recipes/recipe_detail.html', {'recipe': recipe, 'ingredient_list': ingredient_list, 'profile': profile})


@login_required
def recipe_create_view(request, id):
  profile = Profile.objects.get(user=User.objects.get(id=id))
  if request.method == 'POST':
    creator = Profile.objects.get(user=User.objects.get(id=id))
    created_timestamp = datetime.now()
    recipe_name = request.POST.get('recipe_name', '')
    recipe_image = request.FILES.get('recipe_image', 'empty.jpg')
    oven_temp = request.POST.get('oven_temp', '')
    serving_size = request.POST.get('serving_size', '')
    recipe_category = request.POST.get('recipe_category', '')
    recipe_tags = request.POST.get('recipe_tags', '')
    recipe_instructions = request.POST.get('recipe_instructions', '')
    recipe = Recipe(creator=creator, created_timestamp=created_timestamp, recipe_name=recipe_name, recipe_image=recipe_image, oven_temp=oven_temp, serving_size=float(serving_size), recipe_category=recipe_category, recipe_tags=recipe_tags, recipe_instructions=recipe_instructions)
    recipe.save()
    bIndex = str(request.POST).find('ingredient_name_')
    ingredient_count = (str(request.POST)[bIndex+16:bIndex+17])
    for i in range(0, int(ingredient_count) + 1):
      ingredient_name = request.POST.get('ingredient_name_' + str(i), 'didnt work')
      ingredient_quantitiy = request.POST.get('ingredient_quantitiy_' + str(i), '0')
      ingredient_measurement = request.POST.get('ingredient_measurement_' + str(i), '')
      new_ingredient = Ingredient(recipe=recipe, ingredient_name=ingredient_name, ingredient_quanitiy=float(ingredient_quantitiy), ingredient_measurement=ingredient_measurement)
      new_ingredient.save()
    return redirect("recipies:my_recipes", id=id)
  return render(request, 'recipes/create_recipe.html', {'profile': profile})

@login_required
def recipe_update_view(request, id):
  recipe = Recipe.objects.get(pk=id)
  ingredient_list = Ingredient.objects.filter(recipe=recipe.id)
  profile = recipe.creator
  user_id = recipe.creator.id
  if request.method == 'POST':
    image_path = recipe.recipe_image.path
    if os.path.exists(image_path):
      os.remove(image_path)
    creator = Profile.objects.get(pk=user_id)
    created_timestamp = recipe.created_timestamp
    updated_timestamp = datetime.now()
    recipe_name = request.POST.get('recipe_name', '')
    recipe_image = request.FILES.get('recipe_image', 'empty.jpg')
    oven_temp = request.POST.get('oven_temp', '')
    serving_size = request.POST.get('serving_size', '')
    recipe_category = request.POST.get('recipe_category', '')
    recipe_tags = request.POST.get('recipe_tags', '')
    recipe_instructions = request.POST.get('recipe_instructions', '')
    newRecipe = Recipe(creator=creator, created_timestamp=created_timestamp, updated_timestamp=updated_timestamp, recipe_name=recipe_name, recipe_image=recipe_image, oven_temp=oven_temp, serving_size=serving_size, recipe_category=recipe_category, recipe_tags=recipe_tags, recipe_instructions=recipe_instructions)
    newRecipe.save()
    recipe.delete()
    return redirect("recipies:my_recipes", id=user_id)
  return render(request, 'recipes/recipe_edit.html', {'recipe': recipe, 'ingredient_list': ingredient_list, 'profile': profile})


@login_required
def recipe_delete_view(request, id):
  recipe = Recipe.objects.get(pk=id)
  profile = recipe.creator
  if request.method == 'POST':
    recipe.delete()
    image_path = recipe.recipe_image.path
    if os.path.exists(image_path):
        os.remove(image_path)
    return redirect("recipies:my_recipes", id=recipe.creator.id)
  return render(request, 'recipes/recipe_delete.html', {'recipe': recipe, 'profile': profile})