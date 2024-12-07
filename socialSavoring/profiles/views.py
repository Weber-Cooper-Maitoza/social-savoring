from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.
def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    print(form)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Welcome {username}! Your account is created.')
      return redirect('login')
  else: 
    form = RegistrationForm()
  return render(request, 'profiles/register.html', {'form':form})  

@login_required
def settings(request, id):
  profile = Profile.objects.get(user=User.objects.get(id=id))
  return render(request, 'profiles/settings.html', {'profile':profile})

@login_required
def my_profile(request, id):
  profile = Profile.objects.get(user=User.objects.get(id=id))
  return render(request, 'profiles/settings.html', {'profile':profile})