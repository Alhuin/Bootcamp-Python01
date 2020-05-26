class InitRecipeError(Exception):
    messages = {
        "name": "Name can't be empty",
        "cooking_lvl": "Cooking level must be in between 1 and 5",
        "cooking_time": "Cooking time can't be less than 1 minute",
        "ingredients": "Ingredients' list can't be empty",
        "recipe_type": "Recipe_type must be in ['starter', 'lunch', 'dessert']"
    }

    def __init__(self, field):
        self.message = f"Recipe Init Error: {self.messages[field]}."
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
        if name == "":
            raise InitRecipeError("name")
        elif cooking_lvl < 1 or cooking_lvl > 5:
            raise InitRecipeError("cooking_lvl")
        elif cooking_time < 0:
            raise InitRecipeError("cooking_time")
        elif len(ingredients) == 0:
            raise InitRecipeError("ingredients")
        elif recipe_type not in ["starter", "lunch", "dessert"]:
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
