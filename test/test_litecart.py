import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures('setup_teardown_shop')
class TestAdmin():

    def test_links_clickable(self):
        self.login('admin', 'gl_admin')
        items = self.driver.find_elements(By. XPATH, "//ul[@id='box-apps-menu']/li/a")
        items_count = len(items)
        for i in range(items_count):
            self.driver.find_element(By. XPATH, f"//ul[@id='box-apps-menu']/li[{i+1}]/a").click()
            assert EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.panel-heading')), items[i].text + ' item was not correctly opened'
            subitems = self.driver.find_elements(By. XPATH, "//li[@class='app selected']/ul/li/a")
            subitems_count = len(subitems)
            for j in range(subitems_count):
                self.driver.find_element(By.XPATH, f"//li[@class='app selected']/ul/li[{j+1}]/a").click()
                assert EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.panel-heading')), subitems[j].text + ' item was not correctly opened'

    def test_links_opened_in_new_window(self):
        self.login('admin', 'gl_admin')
        self.open_menu_item_by_url('Countries')
        self.open_edit_country_page_by_number(1)
        links = self.driver.find_elements(By.CSS_SELECTOR, '.fa-external-link')
        main_window = self.driver.window_handles[0]
        for l in links:
            l.click()
            assert len(self.driver.window_handles) == 2
            new_window = self.driver.window_handles[1]
            self.driver.switch_to.window(new_window)
            self.driver.close()
            self.driver.switch_to.window(main_window)

    def login(self, user:str, password:str):
        self.driver.get('http://3.122.51.38/litecart/admin')
        self.driver.find_element_by_name('username').send_keys(user)
        self.driver.find_element_by_name('password').send_keys(password + Keys.ENTER)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'sidebar')))

    def open_menu_item_by_url(self, text:str):
        locator = (By.XPATH, f"//ul[@id='box-apps-menu']/li//*[contains(text(), '{text}')]/parent::a")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        el = self.driver.find_element(*locator)
        url = el.get_attribute('href')
        self.driver.get(url)

    def open_edit_country_page_by_number(self, number:int):
        locator = (By.XPATH, f"//form[@name='countries_form']//tbody/tr[{number}]/td/a")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)