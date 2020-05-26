from datetime import datetime
from recipe import Recipe


class AddRecipeError(Exception):
    pass


class InitBookError(Exception):
    def __init__(self, field):
        self.message = f"Recipe Book Error: Invalid {field} field."
    pass


class GetRecipeError(Exception):
    messages = {
        "name": "Unknown recipe name",
        "types": "Unknown recipe type",
    }

    def __init__(self, query):
        self.message = f"Get Recipe Error: {self.messages[query]}."
    pass


class Book:
    """A representation of a book.

    :param name: The book's name.
    :param recipes_list: A 3 keys dict ["starter", "lunch", "dessert"]
    """
    def __init__(self, name, recipes_list):
        if isinstance(name, str) is False or name == "":
            raise InitBookError("name")
        elif isinstance(recipes_list, dict) is False:
            raise InitBookError("recipes_list")

        self.name: str = name
        self.recipes_list: dict = recipes_list
        self.last_update: datetime = datetime.now()
        self.creation_date: datetime = datetime.now()

    def __str__(self):
        return f"{self.name.capitalize()} book:\n" \
               + f"\tRecipes:\t{[key for key in self.recipes_list.keys()]}\n" \
               + f"\tCreation:\t{self.creation_date}\n" \
               + f"\tLast Update:\t{self.last_update}\n"

    def get_recipe_by_name(self, name):
        """ Print a recipe with the name `name` and return the instance """
        for recipe_type in self.recipes_list:
            if name in self.recipes_list[recipe_type]:
                recipe = self.recipes_list[recipe_type][name]
                print(recipe)
                return recipe

        raise GetRecipeError("name")

    def get_recipes_by_types(self, recipe_type):
        """ Get all recipe names for a given recipe_type """
        try:
            return list(self.recipes_list[recipe_type].keys())
        except KeyError:
            raise GetRecipeError("types")

    def add_recipe(self, recipe):
        """ Add a recipe to the book and update last_update """
        if isinstance(recipe, Recipe) is False:
            raise AddRecipeError
        if recipe.name not in self.recipes_list[recipe.recipe_type]:
            self.recipes_list[recipe.recipe_type][recipe.name] = recipe
        else:
            raise AddRecipeError
