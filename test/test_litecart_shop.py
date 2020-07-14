import pytest
from litecart.pages.shop.main import MainPage


@pytest.mark.usefixtures('setup_teardown_shop')
class TestShop():

    def test_add_remove_items_to_cart(self):
        shop = MainPage(self.driver)
        shop.open()
        shop.add_to_cart_total_items(3)
        cart = shop.open_cart()
        cart.remove_cart_items_one_by_one()
        cart.assert_empty()









