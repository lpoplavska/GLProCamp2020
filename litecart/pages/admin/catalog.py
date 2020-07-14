from selenium.webdriver.common.by import By
from litecart.pages.admin.admin import Admin
from litecart.pages.admin.product import Product
from litecart.pages.base import BasePage

class Catalog(BasePage):

    def open(self):
        Admin(self.driver).open_menu_item('Catalog')
        return self

    def add_new_product(self):
        self.driver.find_element(By.CSS_SELECTOR, '.panel-action>.list-inline>li:nth-of-type(2)>a').click()
        return Product(self.driver)

    def get_number_of_products(self):
        footer = self.driver.find_element(By.XPATH, "//*[@name='catalog_form']//tfoot").text
        return int(footer.split(' ')[-1])

    def delete_last_product(self):
        self.driver.find_element(By.XPATH, "//*[@name='catalog_form']//tbody/tr[last()]/td[1]/input").click()
        self.driver.find_element(By.NAME, 'delete').click()
        self.driver.switch_to.alert.accept()

