import pytest

from ingredient import Ingredient
from data import IngredientData


class TestIngredient():

    @pytest.mark.parametrize('ingredient_type,ingredient_name,ingredient_price',
                             [
                                 (IngredientData.INGREDIENT_TYPE[0], IngredientData.INGREDIENT_NAME[0],
                                  IngredientData.INGREDIENT_PRICE[0]),
                                 (IngredientData.INGREDIENT_TYPE[1], IngredientData.INGREDIENT_NAME[1],
                                  IngredientData.INGREDIENT_PRICE[1])
                             ]
                             )
    def test_create_ingredient_created_successfully(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type=ingredient_type, name=ingredient_name, price=ingredient_price)
        assert ingredient.type == ingredient_type and ingredient.name == ingredient_name and ingredient.price == ingredient_price

    @pytest.mark.parametrize('ingredient_type,ingredient_name,ingredient_price',
                             [
                                 (IngredientData.INGREDIENT_TYPE[0], IngredientData.INGREDIENT_NAME[0],
                                  IngredientData.INGREDIENT_PRICE[0]),
                                 (IngredientData.INGREDIENT_TYPE[1], IngredientData.INGREDIENT_NAME[1],
                                  IngredientData.INGREDIENT_PRICE[1])
                             ]
                             )
    def test_get_price_returned_correct_ingredient_price(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type=ingredient_type, name=ingredient_name, price=ingredient_price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize('ingredient_type,ingredient_name,ingredient_price',
                             [
                                 (IngredientData.INGREDIENT_TYPE[0], IngredientData.INGREDIENT_NAME[0],
                                  IngredientData.INGREDIENT_PRICE[0]),
                                 (IngredientData.INGREDIENT_TYPE[1], IngredientData.INGREDIENT_NAME[1],
                                  IngredientData.INGREDIENT_PRICE[1])
                             ]
                             )
    def test_get_price_returned_correct_ingredient_price(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type=ingredient_type, name=ingredient_name, price=ingredient_price)
        assert ingredient.get_name() == ingredient_name

    @pytest.mark.parametrize('ingredient_type,ingredient_name,ingredient_price',
                             [
                                 (IngredientData.INGREDIENT_TYPE[0], IngredientData.INGREDIENT_NAME[0],
                                  IngredientData.INGREDIENT_PRICE[0]),
                                 (IngredientData.INGREDIENT_TYPE[1], IngredientData.INGREDIENT_NAME[1],
                                  IngredientData.INGREDIENT_PRICE[1])
                             ]
                             )
    def test_get_price_returned_correct_ingredient_price(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type=ingredient_type, name=ingredient_name, price=ingredient_price)
        assert ingredient.get_price() == ingredient_price
