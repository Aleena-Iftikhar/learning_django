from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def recipes(request):
    if request.method == "POST":

     data = request.POST
     name = data.get('recipe_name')
     description = data.get("description")
     image = request.FILES.get('image')

     recipe.objects.create(
        recipe_name = name,
        description = description,
        image = image,
     )

     return redirect('recipes')

    return render(request, 'recipes.html')