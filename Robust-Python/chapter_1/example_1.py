class Recipe1:
    def abjust_recipe(recipe, servings):
        new_recipe = [servings]
        old_servings = recipe[0]
        factor = servings / old_servings
        recipe.pop(0)
        while recipe:
            ingredient, amount, unit = recipe.pop(0)
            new_recipe.append((ingredient, amount * factor, unit))
        return new_recipe


class Recipe2:
    def abjust_recipe(recipe, servings):
        old_servings = recipe.pop(0)
        factor = servings / old_servings
        new_recipe = {
            ingredient: (amount * factor, unit) for ingredient, amount, unit in recipe
        }
        new_recipe["servings"] = servings
        return new_recipe


from fractions import Fraction


class Recipe:
    pass


class Recipe3:
    """
    take a meal recipe and change the number of servings
    :param recipe: a `Recipe` indicating what needs to be abusted
    :param servings: the number of servings
    :return Recipe: a recipe with servings size and ingredients adjusted for the new servings
    """

    def abjust_recipe(recipe, servings):
        new_ingredients = list(recipe.get_ingredients())
        recipe.clear_ingredients()

        for ingredient in new_ingredients:
            ingredient.adjust_propoprtion(Fraction(servings, recipe.servings))
        return Recipe(servings, new_ingredients)
