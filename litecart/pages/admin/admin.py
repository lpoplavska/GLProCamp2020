from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from litecart.pages.base import BasePage


class Admin(BasePage):
    def open(self):
        self.driver.get(self.base_url + '/admin')
        return self

    def login(self, user:str, password:str):
        self.driver.find_element_by_name('username').send_keys(user)
        self.driver.find_element_by_name('password').send_keys(password + Keys.ENTER)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'sidebar')))

    def open_menu_item(self, text:str):
        locator = (By.XPATH, f"//ul[@id='box-apps-menu']/li//*[contains(text(), '{text}')]/parent::a")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        el = self.driver.find_element(*locator)
        url = el.get_attribute('href')
        self.driver.get(url)