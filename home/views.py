from django.shortcuts import render

# Create your views here.   
recipes = [
    {'id': 1,
     'name': 'Pancakes',
     'time': 25, 
     'instructions': "Add the ingredients together, then mix in a pan",
     'description': 'Soft and fluffy pancakes',
     'ingredients': ['Flour', 'Eggs', 'Milk', 'Sugar']
    },

    {'id': 2,
     'name': 'Fries',
     'time': 15,
     'instructions': "Clean and cut the potato, sprinkle salt and black pepper, and fry",
     'description': 'Crispy warm fries',
     'ingredients': ['Salt', 'Sweet Potato', 'Black Pepper', 'Oil']
    },

    {'id': 3,
     'name': 'Chicken Nuggets',
     'time': 35,
     'instructions': "Season the chicken properly and deep fry in hot oil",
     'description': 'Crunchy, spiced nuggets',
     'ingredients': ['Chicken Breast', 'Oil', 'Salt', 'Seasoning']
    }

]


def index(request):

    context = {
        'recipes': recipes
    }

    return render(request, 'home/index.html', context)

def recipe_detail(request, recipe_id):
    recipe = None

    for item in recipes:
        if item["id"] == recipe_id:
            recipe = item
            break

    if recipe is None:
        return render(request, 'home/recipe_not_found.html', status=404)

    return render(request, 'home/recipe_detail.html', {'recipe': recipe})
