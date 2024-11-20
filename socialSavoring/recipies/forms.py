from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, Ingredient

class RecipeForm(forms.ModelForm):
  class Meta:
    model = Recipe
    # TODO: add fields
    fields = []
