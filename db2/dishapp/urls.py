
from django.urls import path
from . import views

urlpatterns = [
    
    path("recipe/", views.recipe_create , name='recipe'),
    path("ingredient/", views.ingredient_create , name='ingredient'),
    path("category/", views.category_create, name='category'),
    path("insertRecipe/", views.insertRecipe, name='insertRecipe'),
    path("insertIngredient/", views.insertIngredient, name='insertIngredient'),
    path("insertCategory/", views.insertCategory, name='insertCategory'),
]
