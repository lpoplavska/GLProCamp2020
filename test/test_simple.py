import pytest
from selenium.webdriver.common.keys import Keys

"""
    Select below the needed fixture depending on the method of searching for webdriver file 
    and uncomment the non-relevant fixtures
"""
#@pytest.mark.usefixtures('setup_teardown')
#@pytest.mark.usefixtures('setup_teardown_local')
#@pytest.mark.usefixtures('setup_teardown_wd_manager')
@pytest.mark.usefixtures('setup_teardown_selenium_server')
class TestSimple:

    def test_simple1(self):
        self.driver.get('http://google.com')
        self.driver.find_element_by_name('q').send_keys('Selenium'+Keys.ENTER)
        assert 'Selenium' in self.driver.find_element_by_tag_name('h3').text

    def test_simple2(self):
        self.driver.get('http://google.com')
        self.driver.find_element_by_name('q').send_keys('GlobalLogic'+Keys.ENTER)
        assert False
