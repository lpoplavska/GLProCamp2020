import os
import time
import uuid

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from litecart.pages.base import BasePage


class Product(BasePage):

    def fill_general_tab(self):
        self.open_general()
        self.driver.find_element(By.XPATH, '//*[contains(text(), " Enabled")]').click()
        self.driver.find_element(By.NAME, "name[en]").send_keys(str(uuid.uuid1()))
        self.driver.find_element(By.NAME, "code").send_keys(int(time.time()))
        self.driver.find_element(By.NAME, "sku").send_keys(int(time.time()))
        self.driver.find_element(By.NAME, "mpn").send_keys(int(time.time()))
        self.driver.find_element(By.NAME, "gtin").send_keys(int(time.time()))
        self.driver.find_element(By.NAME, "taric").send_keys(int(time.time()))
        select = Select(self.driver.find_element(By.NAME, "manufacturer_id"))
        select.select_by_value('1')
        self.driver.find_element(By.NAME, "date_valid_from").send_keys('01012020')
        self.driver.find_element(By.NAME, "date_valid_to").send_keys('01012021')
        self.driver.find_element(By.NAME, "keywords").send_keys('ua')
        image = os.path.abspath("camera.jpg")
        self.driver.find_element(By.NAME, "new_images[]").send_keys(image)

    def fill_information_tab(self):
        self.open_information()
        self.driver.find_element(By.NAME, "short_description[en]").send_keys("Canon Photo Camera")
        text_editor = self.driver.find_element(By.CLASS_NAME, 'trumbowyg-editor')
        text_editor.click()
        text_editor.find_element(By.XPATH, './p').send_keys('This is multiline description.\n Canon photo camera is the best')
        self.driver.find_element(By.NAME, "technical_data[en]").send_keys('Technical Data: ua')
        self.driver.find_element(By.NAME, "head_title[en]").send_keys('Head Title: ua')
        self.driver.find_element(By.NAME, "meta_description[en]").send_keys('meta')

    def fill_prices_tab(self):
        self.open_prices()
        purchase_price = self.driver.find_element(By.NAME, 'purchase_price')
        purchase_price.clear()
        purchase_price.send_keys('12')
        select = Select(self.driver.find_element(By.NAME, 'purchase_price_currency_code'))
        select.select_by_visible_text('Euros')
        self.driver.find_element(By.NAME, 'prices[USD]').send_keys('18')

    def save(self):
        self.driver.find_element(By.NAME, 'save').click()
        return

    def open_general(self):
        self.driver.find_element(By.LINK_TEXT, 'General').click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='tab-general'][not(contains(@style,'display: none'))]")))

    def open_information(self):
        self.driver.find_element(By.LINK_TEXT, 'Information').click()
        WebDriverWait(self.driver, 10).\
            until(EC.presence_of_element_located((By.
                                                  XPATH, "//*[@id='tab-information'][not(contains(@style,'display: none'))]")))
        return self


    def open_attributes(self):
        pass

    def open_prices(self):
        self.driver.find_element(By.LINK_TEXT, 'Prices').click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='tab-prices'][not(contains(@style,'display: none'))]")))
        return self

    def open_options(self):
        pass

    def open_stock(self):
        pass