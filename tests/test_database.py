import pytest

from database import Database
from data import DatabaseData


class TestDatabase:

    def test_create_database_created_successfully(self):
        database = Database()
        buns_number = len(database.buns)
        ingredients_number = len(database.ingredients)
        expected_buns_number = len(DatabaseData.EXPECTED_LIST_OF_BUNS)
        expected_ingredients_number = len(DatabaseData.EXPECTED_LIST_OF_INGREDIENTS)
        assert buns_number == expected_buns_number and ingredients_number == expected_ingredients_number

    def test_available_buns_correct_list_of_bun_names_returned_successfully(self, database):
        list_of_buns = []
        available_buns = database.available_buns()
        for bun in available_buns:
            list_of_buns.append(bun.get_name())
        assert list_of_buns == DatabaseData.EXPECTED_LIST_OF_BUNS

    def test_available_ingredients_correct_list_of_ingredient_names_returned_successfully(self, database):
        list_of_ingredients = []
        available_ingredients = database.available_ingredients()
        for ingredient in available_ingredients:
            list_of_ingredients.append(ingredient.get_name())
        assert list_of_ingredients == DatabaseData.EXPECTED_LIST_OF_INGREDIENTS
