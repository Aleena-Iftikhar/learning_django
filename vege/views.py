from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

# ------- CREATE recipes -----------

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

     return redirect('recipes')            # go to /recipes page
   
   # --------- Get recipe -----------
   queryset = recipe.objects.all()

   if request.GET.get('search'):
      queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))       # 'icontain' will return the recipe in which the search word appear 

   context = {"Recipes": queryset}

   return render(request, 'recipes.html', context)


# ---------- UPDATE recipe --------------

def update_recipe(request, id):
   queryset = recipe.objects.get(id = id)

   if request.method == "POST":
      name = request.POST.get('recipe_name')
      description = request.POST.get("description")
      image = request.FILES.get("image")

      queryset.recipe_name = name
      queryset.description = description

      if image:
         queryset.image = image

      queryset.save()
      return redirect('recipes')

   context = {'Recipes': queryset}
   return render(request, 'updateRecipe.html', context)


# ---------- DELETE recipe ------------

def delete_recipe(request, id):
   queryset = recipe.objects.get(id = id)
   queryset.delete()
   
   return redirect('recipes')