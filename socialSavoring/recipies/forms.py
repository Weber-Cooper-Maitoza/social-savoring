from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, Ingredient

class IngredientForm(forms.ModelForm):
  class Meta:
    model = Ingredient
    exclude = ()

IngredientFormSet = inlineformset_factory(Recipe, Ingredient, form=IngredientForm, extra=1)