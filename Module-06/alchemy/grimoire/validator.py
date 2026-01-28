def validate_ingredients(ingredients: str):
    valid_ingredients = ["fire", "water", "earth", "air"]
    ingredients_list = ingredients.split()
    for ingredient in ingredients_list:
        if ingredient not in valid_ingredients:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
