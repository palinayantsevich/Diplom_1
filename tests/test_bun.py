import pytest

from bun import Bun
from data import BunData


class TestBun:

    @pytest.mark.parametrize('bun_name,bun_price',
                             [
                                 (BunData.BUN_NAME[0], BunData.BUN_PRICE[0]),
                                 (BunData.BUN_NAME[1], BunData.BUN_PRICE[1])
                             ]
                             )
    def test_create_bun_created_successfully(self, bun_name, bun_price):
        bun = Bun(name=bun_name, price=bun_price)
        assert bun.name == bun_name and bun.price == bun_price

    @pytest.mark.parametrize('bun_name,bun_price',
                             [
                                 (BunData.BUN_NAME[0], BunData.BUN_PRICE[0]),
                                 (BunData.BUN_NAME[1], BunData.BUN_PRICE[1])
                             ]
                             )
    def test_get_name_correct_bun_name_returned(self, bun_name, bun_price):
        bun = Bun(name=bun_name, price=bun_price)
        assert bun.get_name() == bun_name

    @pytest.mark.parametrize('bun_name,bun_price',
                             [
                                 (BunData.BUN_NAME[0], BunData.BUN_PRICE[0]),
                                 (BunData.BUN_NAME[1], BunData.BUN_PRICE[1])
                             ]
                             )
    def test_get_price_correct_bun_price_returned(self, bun_name, bun_price):
        bun = Bun(name=bun_name, price=bun_price)
        assert bun.get_price() == bun_price
