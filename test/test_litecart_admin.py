import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from litecart.pages.admin.admin import Admin
from litecart.pages.admin.catalog import Catalog
from litecart.pages.admin.countries import Countries

@pytest.mark.usefixtures('setup_teardown_shop')
class TestAdmin():

    def test_links_clickable(self):
        Admin(self.driver).open().login('admin', 'gl_admin')
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
        Admin(self.driver).open().login('admin', 'gl_admin')
        countries = Countries(self.driver).open()
        countries.open_edit_country_page_by_number(1)
        links = self.driver.find_elements(By.CSS_SELECTOR, '.fa-external-link')
        main_window = self.driver.window_handles[0]
        for l in links:
            l.click()
            assert len(self.driver.window_handles) == 2
            new_window = self.driver.window_handles[1]
            self.driver.switch_to.window(new_window)
            self.driver.close()
            self.driver.switch_to.window(main_window)

    def test_add_new_item(self):
        Admin(self.driver).open().login('admin', 'gl_admin')
        catalog = Catalog(self.driver).open()
        quantity_before = catalog.get_number_of_products()
        product = catalog.add_new_product()
        product.fill_general_tab()
        product.fill_information_tab()
        product.fill_prices_tab()
        product.save()
        quantity_after = catalog.get_number_of_products()
        assert quantity_after == quantity_before + 1
        catalog.delete_last_product()




