from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class BunData:
    BUN_NAME = ['Марсовая булка C-3PO', 'Земляная булка BB-8']
    BUN_PRICE = [999.99, 12999]


class IngredientData:
    INGREDIENT_TYPE = [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]
    INGREDIENT_NAME = ['Космический лиловый халапеньо', 'Инопланетная красная петрушка']
    INGREDIENT_PRICE = [99.99, 1000]


class BurgerData:
    BUN_DEFAULT = None
    INGREDIENTS_DEFAULT = []
    EXPECTED_RECEIPT_BUN_ONE_INGREDIENT = (
        '(==== Марсовая булка C-3PO ====)\n'
        '= sauce Космический лиловый халапеньо =\n'
        '(==== Марсовая булка C-3PO ====)\n'
        '\n'
        'Price: 2099.97'
    )

    EXPECTED_RECEIPT_BUN_TWO_INGREDIENTS = (
        '(==== Марсовая булка C-3PO ====)\n'
        '= sauce Космический лиловый халапеньо =\n'
        '= filling Инопланетная красная петрушка =\n'
        '(==== Марсовая булка C-3PO ====)\n'
        '\n'
        'Price: 3099.97'
    )


class DatabaseData:
    EXPECTED_LIST_OF_BUNS = ['black bun', 'white bun', 'red bun']
    EXPECTED_LIST_OF_INGREDIENTS = ['hot sauce', 'sour cream', 'chili sauce', 'cutlet', 'dinosaur',
                                    'sausage']
