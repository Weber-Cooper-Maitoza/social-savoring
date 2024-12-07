from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from recipies.models import Recipe, Ingredient
from profiles.models import Profile
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# Create your views here.

@login_required
def feed(request, id):
  profile = Profile.objects.get(user=User.objects.get(id=id))
  recipe_list = Recipe.objects.all()
  paginator = Paginator(recipe_list, 3)
  page = request.GET.get('page')
  recipe_list = paginator.get_page(page)
  return render(request, 'socialMedia/feed.html', {"recipe_list": recipe_list, 'profile': profile})


@login_required
def categories(request, id):
  profile = Profile.objects.get(user=User.objects.get(id=id))
  if request.method == 'POST':
    category = request.POST.get('category_search', '')
    print(category)
    recipe_category_list = Recipe.objects.filter(recipe_category=category)
    paginator = Paginator(recipe_category_list, 3)
    page = request.GET.get('page')
    recipe_category_list = paginator.get_page(page)
  else:
   recipe_category_list = None
  return render(request, 'socialMedia/categories.html', {'recipe_category_list': recipe_category_list, 'profile': profile})

@login_required
def detail(request, id):
  recipe = Recipe.objects.get(pk=id)
  profile = recipe.creator
  ingredient_list = Ingredient.objects.filter(recipe=recipe.id)
  return render(request, 'socialMedia/detail.html', {'recipe': recipe, 'ingredient_list': ingredient_list, 'profile': profile})