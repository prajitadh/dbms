from django.db import models


# Create your models here.

class Recipe(models.Model):
    dish_name= models.CharField(max_length=200)
    recipe_name= models.CharField(max_length=100)
    description= models.TextField()
    instruction= models.TextField()
    #ingredients= models.ManyToManyField(Ingredient, blank= True)
  
    def __str__(self):
        return self.dish_name


class Ingredient(models.Model):
    ingredients= models.CharField('Ingredients Names', max_length=500)
    quantity= models.CharField(max_length= 100)
    recipe_id= models.ManyToManyField(Recipe)
    
    def __str__(self):
        return self.ingredients
    
class Category(models.Model):
    category= models.CharField('Category Name', max_length=100)
    recipe_id= models.ForeignKey(Recipe, on_delete=models.CASCADE )
    
    def __str__(self):
        return self.category