import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = None

@pytest.fixture()
def setup_teardown(request):
    global driver
    print('setup method')
    BROWSERSTACK_URL = 'https://liubov14:pxapctrFnTmgLdoUE5yi@hub-cloud.browserstack.com/wd/hub'
    desired_cap = {

        'os': 'Windows',
        'os_version': '8.1',
        'browser': 'Chrome',
        'browser_version': '78',
        'name': "liubov14's First Test",
        'download.default_directory': "/tmp/"
    }

    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap, options=options)
    request.cls.driver = driver
    yield
    print('teardown method')
    driver.quit()