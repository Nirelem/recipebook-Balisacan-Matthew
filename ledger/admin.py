from django.contrib import admin

# Register your models here.
from .models import Ingredient, Recipe, RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)

