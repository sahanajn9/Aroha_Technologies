from django.shortcuts import render
# from .utils import get_recipe_from_groq
from recepiapp.utils import get_recipe_from_groq


# Create your views here.
# def Display(request):
#     return render(request,'base.html')


def recipe_view(request):
    recipe = None
    if request.method == 'POST':
        ingredients = request.POST.get("ingredients").split(",")
        print("Ingredients:", ingredients)
        recipe = get_recipe_from_groq(ingredients)
        print("Recipe from Groq:", recipe)
    return render(request, "base.html", {"recipe": recipe})
    # else:
    #     print("Error....")
