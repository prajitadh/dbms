from django.shortcuts import render
from .models import Recipe, Ingredient, Category
from django.shortcuts import get_object_or_404

# Create your views here.
def recipe_create(request):
    return render(request, 'recipe.html', {})

def ingredient_create(request):
    return render(request, 'ingredient.html', {})

def category_create(request):
    return render(request, 'category.html', {})

#create insert method to post data from template to corresponding models

def insertRecipe(request):
    vdish= request.POST['tdish']
    trname=request.POST['trname']
    tdesc=request.POST['tdesc']
    tinst=request.POST['tinst']
    us=Recipe(dish_name= vdish ,recipe_name= trname,description=tdesc, instruction=tinst )
    us.save()

    return render(request, 'ingredient.html', {})

def insertIngredient(request):
    viname= request.POST['tiname']
    viqua=request.POST['tiqua']
    vidish=request.POST['tidish']
    #recipe = get_object_or_404(Recipe, id=int(vidish))
    ing=Ingredient(ingredients=viname ,quantity= viqua)
    ing.save()

    #recipe.ingredients.add(ing)
    return render(request, 'category.html', {})


def insertCategory(request):
    vcat= request.POST['tcat']
    vcdish=request.POST['tcdish']

    #recipe = get_object_or_404(Recipe, id=int(vcdish))
    cat=Category(category=vcat ,recipe_id= vcdish)
    cat.save()

    return render(request, 'recipe.html', {})
