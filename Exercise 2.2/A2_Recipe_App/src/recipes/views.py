# views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/main.html'

class RecipeDetailView(DetailView):
   model = Recipe
   template_name = 'recipes/detail.html'

def home(request):
    return render(request, 'recipes/recipes_home.html')
