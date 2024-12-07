from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from recipies.models import Recipe, Ingredient
from profiles.models import Profile
from django.views.generic.list import ListView
from django.contrib.auth.models import User

# Create your views here.

@login_required
def feed(request, id):
  profile = Profile.objects.get(user=User.objects.get(id=id))
  recipe_list = Recipe.objects.all()
  return render(request, 'socialMedia/feed.html', {"recipe_list": recipe_list, 'profile': profile})


@login_required
def categories(request, id):
  profile = Profile.objects.get(user=User.objects.get(id=id))
  category = request.POST.get('category')
  recipe_category_list = Recipe.objects.filter(recipe_category=category)
  return render(request, 'socialMedia/categories.html', {'recipe_category_list': recipe_category_list, 'profile': profile})