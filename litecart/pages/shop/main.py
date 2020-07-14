from random import randint
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from litecart.pages.base import BasePage
from litecart.pages.shop.cart import Cart


class MainPage(BasePage):

    def open(self):
        self.driver.get(self.base_url)
        return self

    def add_to_cart_total_items(self, count):
        while self.get_cart_quantity() < count:
            self.add_to_cart(randint(1, 3))

    def add_to_cart(self, index):
        self.driver.find_elements(By.XPATH, "//*[@id='box-popular-products']//*[@class='product-column']")[
            index - 1].click()
        quantity_before = self.get_cart_quantity()
        self.driver.find_element(By.NAME, 'add_cart_product').click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#cart .quantity'), str(quantity_before + 1)))
        self.driver.back()
        return self

    def get_cart_quantity(self):
        q = self.driver.find_element(By.CSS_SELECTOR, '#cart .quantity').text
        return 0 if q == '' else int(q)

    def open_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, '#cart>a').click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='box-checkout-summary']")))
        return Cart(self.driver)
