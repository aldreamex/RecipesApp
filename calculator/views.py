from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'tea': {
        'чай, пакетик': 1,
        'сахар, ложка': 1,
        }
}

def home_list(request):
    template_home_name = 'calculator/home.html'
    return render(request, template_home_name)

def recipe_handler(request, recipe_name):
    template_name = 'calculator/index.html'
    recipe = DATA.get(recipe_name)

    if recipe:
        servings = int(request.GET.get('servings', 1))
        scaled_recipe = {}

        for ingridient, amount  in recipe.items():
            scaled_amount = amount * servings
            scaled_recipe[ingridient] = scaled_amount

            context = {
                'recipe': scaled_recipe,
                'dish_name': recipe_name
            }
    else:
        context = {}

    return render(request, template_name, context)





