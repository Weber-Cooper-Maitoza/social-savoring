from . import views
from django.urls import path

app_name = 'socialMedia'
urlpatterns = [
    path('feed/', views.feed, name="feed"),
    path('categories/', views.categories, name="categories"),
] 