from . import views
from django.urls import path

app_name = 'recipies'
urlpatterns = [
  path('my_recipes/<int:id>', views.recipe_list_view, name='my_recipes'),
  path('create/<int:id>', views.recipe_create_view, name="create"),
]