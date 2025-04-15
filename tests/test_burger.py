import pytest

from burger import Burger
from data import BurgerData, BunData, IngredientData


class TestBurger():
    def test_create_burger_created_successfully(self):
        burger = Burger()
        assert burger.bun == BurgerData.BUN_DEFAULT and burger.ingredients == BurgerData.INGREDIENTS_DEFAULT

    def test_set_buns_bun_set_successfully(self, burger, bun_mock):
        burger.set_buns(bun_mock)
        assert burger.bun.name == bun_mock.name and burger.bun.price == bun_mock.price

    def test_add_one_ingredient_ingredient_added_successfully(self, burger, ingredient_one_mock):
        burger.add_ingredient(ingredient_one_mock)
        number_of_ingredients = len(burger.ingredients)
        assert (ingredient_one_mock.type == burger.ingredients[0].type and ingredient_one_mock.name ==
                burger.ingredients[
                    0].name and ingredient_one_mock.price == burger.ingredients[0].price) and number_of_ingredients == 1

    def test_add_two_ingredients_ingredients_added_successfully(self, burger, ingredient_one_mock,
                                                                ingredient_second_mock):
        burger.add_ingredient(ingredient_one_mock)
        burger.add_ingredient(ingredient_second_mock)
        number_of_ingredients = len(burger.ingredients)
        assert number_of_ingredients == 2

    def test_remove_ingredient_1_of_1_ingredient_removed_successfully(self, burger, ingredient_one_mock):
        burger.add_ingredient(ingredient_one_mock)
        number_of_ingredients = len(burger.ingredients)
        burger.remove_ingredient(number_of_ingredients - 1)
        assert (number_of_ingredients - 1) == 0

    def test_remove_ingredient_1_of_2_ingredient_removed_successfully(self, burger, ingredient_one_mock,
                                                                      ingredient_second_mock):
        burger.add_ingredient(ingredient_one_mock)
        burger.add_ingredient(ingredient_second_mock)
        number_of_ingredients = len(burger.ingredients)
        burger.remove_ingredient(number_of_ingredients - 1)
        assert (number_of_ingredients - 1) == 1

    def test_move_ingredient_ingredients_moved_successfully(self, burger, ingredient_one_mock, ingredient_second_mock):
        burger.add_ingredient(ingredient_one_mock)
        burger.add_ingredient(ingredient_second_mock)
        burger.move_ingredient(1, 0)
        number_of_ingredients = len(burger.ingredients)
        assert number_of_ingredients == 2 and burger.ingredients[1] == ingredient_one_mock

    def test_get_price_bun_and_one_ingredient_price_returned_successfully(self, burger, bun_mock, ingredient_one_mock):
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_one_mock)
        price = burger.get_price()
        expected_price = BunData.BUN_PRICE[0] * 2 + IngredientData.INGREDIENT_PRICE[0]
        assert price == expected_price

    def test_get_price_bun_and_two_ingredients_price_returned_successfully(self, burger, bun_mock, ingredient_one_mock,
                                                                           ingredient_second_mock):
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_one_mock)
        burger.add_ingredient(ingredient_second_mock)
        price = burger.get_price()
        expected_price = BunData.BUN_PRICE[0] * 2 + IngredientData.INGREDIENT_PRICE[0] + \
                         IngredientData.INGREDIENT_PRICE[1]
        assert price == expected_price

    def test_get_receipt_bun_and_one_ingredient_receipt_returned_successfully(self, burger, bun_mock,
                                                                              ingredient_one_mock):
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_one_mock)
        receipt = burger.get_receipt()
        assert receipt == BurgerData.EXPECTED_RECEIPT_BUN_ONE_INGREDIENT

    def test_get_receipt_bun_and_two_ingredients_receipt_returned_successfully(self, burger, bun_mock,
                                                                               ingredient_one_mock,
                                                                               ingredient_second_mock):
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_one_mock)
        burger.add_ingredient(ingredient_second_mock)
        receipt = burger.get_receipt()
        assert receipt == BurgerData.EXPECTED_RECEIPT_BUN_TWO_INGREDIENTS
