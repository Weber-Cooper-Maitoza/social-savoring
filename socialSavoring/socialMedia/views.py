from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from recipies.models import Recipe, Ingredient
from django.views.generic.list import ListView

# Create your views here.

class FeedView(ListView):
  model = Recipe
  template_name = 'socialMedia/feed.html'
  context_object_name = 'recipes'
  paginate_by = 2
  # recipe_list = Recipe.objects.all()
  # return render(request, 'socialMedia/feed.html', {"recipe_list": recipe_list})


@login_required
def categories(request):
  category = request.POST.get('category')
  recipe_category_list = Recipe.objects.filter(recipe_category=category)
  return render(request, 'socialMedia/categories.html', {'recipe_category_list': recipe_category_list})