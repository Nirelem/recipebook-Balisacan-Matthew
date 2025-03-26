from django.shortcuts import render, get_object_or_404
from .models import Recipe, RecipeImage
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
    
def recipes_list(request):
    recipes = Recipe.objects.all() 
    return render(request, 'recipes_list.html', {'recipes': recipes})
    
   
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingredients = recipe.ingredients.all()  
    return render(request, 'recipe_detail.html', {'recipe': recipe, 'ingredients': ingredients})

class RecipeCreateView(CreateView):
    model = Recipe
    fields = ['name']
    template_name= 'create_recipe.html'
    success_url = reverse_lazy('ledger:recipes_list')

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class RecipeImageCreateView(CreateView):
    model = RecipeImage
    fields = ['image', 'description']
    template_name = 'add_recipe_image.html'

    def form_valid(self, form):
        form.instance.recipe_id = self.kwargs['pk']  
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ledger:recipe_detail', kwargs={'recipe_id': self.kwargs['pk']})