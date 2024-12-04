from . import views
from django.urls import path

app_name = 'recipies'
urlpatterns = [
  path('my_recipes/<int:id>', views.recipe_list_view, name='my_recipes'),
  path('create/<int:id>', views.recipe_create_view, name="create"),
  path('recipe_detail/<int:id>', views.recipe_detail_view, name="recipe_detail"),
  path('recipe_edit/<int:id>', views.recipe_update_view, name="recipe_edit"),
  path('recipe_delete/<int:id>', views.recipe_delete_view, name="recipe_delete"),
]