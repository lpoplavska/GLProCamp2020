from random import random, randint

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures('setup_teardown_shop')
class TestShop():

    def test_add_remove_items(self):
        self.driver.get('http://3.122.51.38/litecart/')
        self.add_to_cart_total_items(3)
        self.open_cart()
        self.remove_cart_items_one_by_one()
        assert self.driver.find_element(By.CSS_SELECTOR, '#content>p').text == 'There are no items in your cart.'

    def add_to_cart_total_items(self, count):
        while self.get_cart_quantity() < count:
            self.add_to_cart(randint(1, 3))

    def add_to_cart(self, index):
        self.driver.find_elements(By.XPATH, "//*[@id='box-popular-products']//*[@class='product-column']")[index-1].click()
        quantity_before = self.get_cart_quantity()
        self.driver.find_element(By.NAME, 'add_cart_product').click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#cart .quantity'), str(quantity_before + 1)))
        self.driver.back()

    def get_cart_quantity(self):
        q = self.driver.find_element(By.CSS_SELECTOR, '#cart .quantity').text
        return 0 if q == '' else int(q)

    def open_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, '#cart>a').click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='box-checkout-summary']")))

    def get_cart_items(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "#box-checkout-cart tbody>tr")

    def get_subtotal(self):
        return float(
            self.driver.find_element(By.XPATH, "//*[@id='box-checkout-summary']//tbody/tr[1]/td[2]").text.lstrip(
                '$'))

    def remove_cart_items_one_by_one(self):
        items = self.get_cart_items()
        for i in range(len(items) - 1):
            subtotal_before = self.get_subtotal()
            sum_for_item = self.remove_first_item_from_cart()
            assert self.get_subtotal() - (subtotal_before - sum_for_item) == 0
        self.remove_last_item_from_cart()

    def remove_last_item_from_cart(self):
        item = self.driver.find_elements(By.CSS_SELECTOR, "#box-checkout-cart tbody>tr")[0]
        item.find_element(By.XPATH, ".//button[@name='remove_cart_item']").click()
        WebDriverWait(self.driver, 10). \
            until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#content>p')))

    def remove_first_item_from_cart(self):
        item = self.driver.find_elements(By.CSS_SELECTOR, "#box-checkout-cart tbody>tr")[0]
        sum_for_item = float(item.find_element(By.XPATH, "./td[last()-1]").text.lstrip('$'))
        item.find_element(By.XPATH, ".//button[@name='remove_cart_item']").click()
        subtotal_element = self.driver.find_element(By.XPATH, "//*[@id='box-checkout-summary']")
        WebDriverWait(self.driver, 10).until(EC.staleness_of(subtotal_element))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='box-checkout-summary']")))
        return sum_for_item





