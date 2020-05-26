class InitRecipeError(Exception):
    def __init__(self, field):
        self.message = f"Recipe Init Error: Invalid {field} field."
    pass


class Recipe:
    """A representation of a recipe.

    :param name: The recipe's name.
    :param cooking_lvl: The recipe's difficulty, from 1 to 5.
    :param cooking_time: The recipe's time to cook in minutes, no negative.
    :param ingredients: List of all ingredients each represented by a string.
    :param description: The recipe's descripton.
    :param recipe_type: Can be "starter", "lunch" or "dessert".
    """
    def __init__(self, name, cooking_lvl, cooking_time, ingredients,
                 description, recipe_type):
        if isinstance(name, str) is False or name == "":
            raise InitRecipeError("name")
        elif isinstance(cooking_lvl, int) is False \
                or cooking_lvl < 1 or cooking_lvl > 5:
            raise InitRecipeError("cooking_lvl")
        elif isinstance(cooking_time, int) is False or cooking_time < 0:
            raise InitRecipeError("cooking_time")
        elif isinstance(ingredients, list) is False or len(ingredients) == 0:
            raise InitRecipeError("ingredients")
        elif isinstance(recipe_type, str) is False \
                or recipe_type not in ["starter", "lunch", "dessert"]:
            raise InitRecipeError("recipe_type")

        self.name: str = name
        self.cooking_lvl: int = cooking_lvl
        self.cooking_time: int = cooking_time
        self.ingredients: list = ingredients
        self.description: str = description
        self.recipe_type: str = recipe_type

    def __str__(self):
        return f"{self.name.capitalize()} recipe:\n"\
               + f"\tDescription:\t\t{self.description}\n"\
               + f"\tType:\t\t\t{self.recipe_type}\n"\
               + f"\tDifficulty:\t\t{self.cooking_lvl}\n"\
               + f"\tAverage cooking time:\t{self.cooking_time} minutes\n"\
               + f"\tingredients:\t\t{self.ingredients}\n"
