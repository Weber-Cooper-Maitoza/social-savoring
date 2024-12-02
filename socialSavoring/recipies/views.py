from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Recipe, Ingredient
from profiles.models import Profile
from datetime import datetime

# Create your views here.

@login_required
def recipe_list_view(request, id):
  user = Profile.objects.get(pk=id)
  recipes = Recipe.objects.filter(creator=user)
  for i in recipes:
    print(i.recipe_name)
  return render(request, 'recipes/my_recipes.html', {'recipes': recipes})


@login_required
def recipe_detail_view(request, id):
  recipe = Recipe.objects.get(pk=id)
  return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


@login_required
def recipe_create_view(request, id):
  if request.method == 'POST':
    # creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    creator = Profile.objects.get(pk=id)
    created_timestamp = datetime.now()
    recipe_name = request.POST.get('recipe_name', '')
    # recipe_image = models.CharField(max_length=500, default="")
    # recipe_image = request.POST.get('recipe_image', '')
    oven_temp = request.POST.get('oven_temp', '')
    serving_size = request.POST.get('oven_temp', '')
    recipe_category = request.POST.get('recipe_category', '')
    recipe_tags = request.POST.get('recipe_tags', '')
    recipe_instructions = request.POST.get('recipe_instructions', '')
    recipe = Recipe(creator=creator, created_timestamp=created_timestamp, recipe_name=recipe_name, oven_temp=oven_temp, serving_size=serving_size, recipe_category=recipe_category, recipe_tags=recipe_tags, recipe_instructions=recipe_instructions)
    recipe.save()

    
  return render(request, 'recipes/create_recipe.html')


@login_required
def recipe_update_view(request, id=None):
  recipe = Recipe.objects.get(pk=id)
  form = RecipeForm(request.POST or None, instance=recipe)

  if form.is_valid():
    form.save()
    # return redirect('food:index')
  
  return render(request, 'food/item-form.html', {'form':form, 'recipe':recipe})

@login_required
def recipe_delete_view(request, id=None):
  recipe = Recipe.objects.get(pk=id)

  if request.method == 'POST':
    recipe.delete()
    # return redirect('food:index')

  return render(request, 'food/item-delete.html', {'recipe':recipe})