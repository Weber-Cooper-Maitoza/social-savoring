from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

app_name = 'socialMedia'
urlpatterns = [
    path('feed/', login_required(views.FeedView.as_view()), name="feed"),
    path('categories/', views.categories, name="categories"),
] 