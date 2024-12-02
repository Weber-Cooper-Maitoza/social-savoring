from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def feed(request):
  return render(request, 'socialMedia/feed.html')

@login_required
def categories(request):
  return render(request, 'socialMedia/categories.html')