from . import views
from django.urls import path

app_name = 'socialMedia'
urlpatterns = [
    path('feed/', views.feed, name="feed"),
]