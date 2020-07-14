from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from litecart.pages.admin.admin import Admin
from litecart.pages.base import BasePage


class Countries(BasePage):
    
    def open(self):
        Admin(self.driver).open_menu_item('Countries')
        return self

    def open_edit_country_page_by_number(self, number:int):
        locator = (By.XPATH, f"//form[@name='countries_form']//tbody/tr[{number}]/td/a")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)