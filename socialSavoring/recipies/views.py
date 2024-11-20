from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Recipe, Ingredient
from .forms import RecipeForm

# Create your views here.

@login_required
def recipe_list_view(request,):
  recipes = Recipe.objects.filter(creator=request.user)
  return render(request, 'recipes/my_recipes.html', {'recipes': recipes})


@login_required
def recipe_detail_view(request, id):
  recipe = Recipe.objects.get(pk=id)
  return render(request, 'recipes/post.html', {'recipe': recipe})


@login_required
def recipe_create_view(request, id=None):
  form = RecipeForm(request.POST or None)
  pass


@login_required
def recipe_update_view(request, id=None):
  pass