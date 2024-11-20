from django.contrib import admin
from django.contrib.auth.models import User
from django.forms import BaseInlineFormSet
from .models import Profile

# Register your models here.

admin.site.register(Profile)