from django.urls import path

from .views import recipes_list, recipe_detail, RecipeCreateView, RecipeImageCreateView

urlpatterns = [
    path('recipe/<int:pk>/add_image/', RecipeImageCreateView.as_view(), name='add_recipe_image'),
    path('add/', RecipeCreateView.as_view(), name='add_recipe'),
    path('', recipes_list, name='recipes_list'),
    path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
]

app_name = "ledger"