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
        if name == ""\
                or cooking_lvl < 1\
                or cooking_lvl > 5\
                or cooking_time < 0\
                or len(ingredients) == 0\
                or recipe_type not in ["starter", "lunch", "dessert"]:
            raise ValueError

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


r = Recipe(
    "test",
    2,
    30,
    ['eggs', "flour"],
    "description",
    "starter"
)

print(str(r))
