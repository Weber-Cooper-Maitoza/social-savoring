from . import views
from django.urls import path

app_name = 'profiles'
urlpatterns = [
  path('register/', views.register, name='register'),
  path('settings/<int:id>', views.settings, name="settings"),
  path('my_profile/<int:id>', views.my_profile, name="my_profile"),
]