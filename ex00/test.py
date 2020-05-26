import unittest

from book import Book, GetRecipeError, AddRecipeError
from recipe import Recipe, InitRecipeError


class TestInitRecipe(unittest.TestCase):
    def test_empty_name(self):
        with self.assertRaises(InitRecipeError):
            Recipe(
                name="",
                cooking_lvl=2,
                cooking_time=20,
                ingredients=["sugar", "flour"],
                description="",
                recipe_type="starter"
            )

    def test_cooking_lvl_oor(self):
        with self.assertRaises(InitRecipeError):
            Recipe(
                name="recipe_one",
                cooking_lvl=-1,
                cooking_time=20,
                ingredients=["sugar", "flour"],
                description="",
                recipe_type="starter"
            )

    def test_negative_cooking_time(self):
        with self.assertRaises(InitRecipeError):
            Recipe(
                name="recipe_one",
                cooking_lvl=2,
                cooking_time=-1,
                ingredients=["sugar", "flour"],
                description="",
                recipe_type="starter"
            )

    def test_no_ingredients(self):
        with self.assertRaises(InitRecipeError):
            Recipe(
                name="recipe_one",
                cooking_lvl=2,
                cooking_time=20,
                ingredients=[],
                description="",
                recipe_type="starter"
            )

    def test_wrong_recipe_type(self):
        with self.assertRaises(InitRecipeError):
            Recipe(
                name="recipe_one",
                cooking_lvl=2,
                cooking_time=20,
                ingredients=["sugar", "flour"],
                description="",
                recipe_type="drink"
            )

    def test_good_params(self):
        recipe = Recipe(
            name="recipe_one",
            cooking_lvl=2,
            cooking_time=20,
            ingredients=["sugar", "flour"],
            description="",
            recipe_type="starter"
        )
        self.assertEqual(recipe.name, "recipe_one")
        self.assertEqual(recipe.cooking_lvl, 2)
        self.assertEqual(recipe.cooking_time, 20)
        self.assertEqual(recipe.ingredients, ["sugar", "flour"])
        self.assertEqual(recipe.description, "")
        self.assertEqual(recipe.recipe_type, "starter")


class TestBookMethods(unittest.TestCase):
    def setUp(self):
        self.recipe_one = Recipe(
            name="recipe_one",
            cooking_lvl=2,
            cooking_time=20,
            ingredients=["sugar", "flour"],
            description="",
            recipe_type="starter"
        )
        self.cook_book = Book(
            name="Test cookBook",
            recipes_list=dict({
                "starter": {},
                "lunch": {},
                "dessert": {},
            }),
        )

    def test_add_recipe(self):
        self.cook_book.add_recipe(self.recipe_one)
        self.assertDictEqual(
            self.cook_book.recipes_list[self.recipe_one.recipe_type],
            dict({self.recipe_one.name: self.recipe_one})
        )
        with self.assertRaises(AddRecipeError):
            self.cook_book.add_recipe(self.recipe_one)
            self.cook_book.add_recipe(self.recipe_one)

        with self.assertRaises(AddRecipeError):
            self.cook_book.add_recipe("")

    def test_get_recipe_by_name(self):
        with self.assertRaises(GetRecipeError):
            self.cook_book.get_recipe_by_name("recipe_one")

        self.cook_book.add_recipe(self.recipe_one)
        recipe = self.cook_book.get_recipe_by_name("recipe_one")
        self.assertEqual(recipe, self.recipe_one)

    def test_get_recipe_by_types(self):
        with self.assertRaises(GetRecipeError):
            self.cook_book.get_recipes_by_types("drink")

        recipes = self.cook_book.get_recipes_by_types("starter")
        self.assertEqual(
            recipes,
            [],
        )

        self.cook_book.add_recipe(self.recipe_one)
        recipes = self.cook_book.get_recipes_by_types("starter")
        self.assertEqual(
            recipes,
            [self.recipe_one.name]
        )


if __name__ == "__main__":
    unittest.main()
