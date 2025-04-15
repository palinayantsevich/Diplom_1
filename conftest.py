import pytest

from unittest.mock import Mock

from burger import Burger
from database import Database
from data import BunData, IngredientData


@pytest.fixture(scope='function')
def bun_mock():
    bun_mock = Mock()
    bun_mock.name = BunData.BUN_NAME[0]
    bun_mock.price = BunData.BUN_PRICE[0]
    bun_mock.get_name.return_value = BunData.BUN_NAME[0]
    bun_mock.get_price.return_value = BunData.BUN_PRICE[0]
    return bun_mock


@pytest.fixture(scope='function')
def ingredient_one_mock():
    ingredient_one_mock = Mock()
    ingredient_one_mock.type = IngredientData.INGREDIENT_TYPE[0]
    ingredient_one_mock.name = IngredientData.INGREDIENT_NAME[0]
    ingredient_one_mock.price = IngredientData.INGREDIENT_PRICE[0]
    ingredient_one_mock.get_type.return_value = IngredientData.INGREDIENT_TYPE[0]
    ingredient_one_mock.get_name.return_value = IngredientData.INGREDIENT_NAME[0]
    ingredient_one_mock.get_price.return_value = IngredientData.INGREDIENT_PRICE[0]
    return ingredient_one_mock


@pytest.fixture(scope='function')
def ingredient_second_mock():
    ingredient_second_mock = Mock()
    ingredient_second_mock.type = IngredientData.INGREDIENT_TYPE[1]
    ingredient_second_mock.name = IngredientData.INGREDIENT_NAME[1]
    ingredient_second_mock.price = IngredientData.INGREDIENT_PRICE[1]
    ingredient_second_mock.get_type.return_value = IngredientData.INGREDIENT_TYPE[1]
    ingredient_second_mock.get_name.return_value = IngredientData.INGREDIENT_NAME[1]
    ingredient_second_mock.get_price.return_value = IngredientData.INGREDIENT_PRICE[1]
    return ingredient_second_mock


@pytest.fixture(scope='function')
def burger():
    burger = Burger()
    yield burger


@pytest.fixture(scope='function')
def database():
    database = Database()
    yield database
