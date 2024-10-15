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
    'okroshka':{}
    # можете добавить свои рецепты ;)
}

def recipe_view(request, dish):
    recipe = DATA.get(dish)  # Получаем рецепт по имени блюда

    servings = int(request.GET.get('servings', 1))

    # Умножаем количество ингредиентов на количество порций и округлаем до двух знаков после запятой,
    # т.к. при количестве, например, 82 персоны для омлета значение будет равно 8.200000000000001 :)
    if recipe:
        recipe_for_servings = {ingredient: round(amount * servings, 2) for ingredient, amount in recipe.items()}
    else:
        recipe_for_servings = {}
    context = {
        'recipe': recipe_for_servings,
    }

    return render(request, 'calculator/index.html', context)