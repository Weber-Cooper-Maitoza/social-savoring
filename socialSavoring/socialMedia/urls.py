from . import views
from django.urls import path

app_name = 'socialMedia'
urlpatterns = [
    path('feed/<int:id>', views.feed, name="feed"),
    path('categories/<int:id>', views.categories, name="categories"),
    path('recipe_detail/<int:id>', views.detail, name='recipe_detail')
] 