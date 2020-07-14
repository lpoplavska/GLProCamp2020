import uuid

from selenium.webdriver.common.by import By
from litecart.pages.base import BasePage

class General(BasePage):

    def enable(self):
        self.driver.find_element(By.XPATH, '//*[contains(text(), " Enabled")]').click()

    def disable(self):
        self.driver.find_element(By.XPATH, '//*[contains(text(), " Disabled")]').click()

    def fill_name(self, text):
        self.driver.find_element(By.XPATH, "//label[contains(text(),'Name')]/parent::div//input").send_keys(uuid.uuid1())
