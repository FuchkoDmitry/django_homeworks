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
}


def dishes_view(request):
    context = {'dishes': DATA.keys()}
    return render(request, 'calculator/home.html', context)


def recipe_view(request, dish):
    servings = int(request.GET.get('servings', 1))
    recipe = DATA.get(dish)
    if servings > 1:
        for ingredients in recipe:
            recipe[ingredients] *= servings

    context = {'recipe': recipe,
               'servings': servings}
    return render(request, 'calculator/index.html', context)
