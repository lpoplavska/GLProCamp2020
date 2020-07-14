import pytest
from selenium import webdriver
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager

simple_driver = None

@pytest.fixture()
def setup_teardown_browserstack(request):
    """
    Fixture to setup webdriver using browserstack
    :param request:
    :return:
    """
    global simple_driver
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
    simple_driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap, options=options)
    request.cls.simple_driver = simple_driver
    yield
    print('teardown method')
    simple_driver.quit()

@pytest.fixture()
def setup_teardown_local(request):
    """
    Fixture to setup webdriver location as project directory
    :param request:
    :return:
    """
    global simple_driver
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    simple_driver = webdriver.Chrome(options=options)
    request.cls.simple_driver = simple_driver
    yield
    print('teardown method')
    simple_driver.quit()

@pytest.fixture()
def setup_teardown_wd_manager(request):
    """
    Fixture to setup webdriver by webdriver manager
    :param request:
    :return:
    """
    global simple_driver
    options = webdriver.ChromeOptions()

    #To initialize Firefox driver comment the previous line and uncomment the next line of code
    #options = webdriver.FirefoxOptions()
    options.add_argument('--start-maximized')
    simple_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # To use Firefox driver comment the previous line and uncomment the next line of code
    #driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    request.cls.simple_driver = simple_driver
    yield
    print('teardown method')
    simple_driver.quit()

@pytest.fixture()
def setup_teardown_selenium_server(request):
    """
    Fixture to setup webdriver by selenium server (Grid)
    :param request:
    :return:
    """
    global simple_driver
    options = webdriver.ChromeOptions()

    #To initialize Firefox driver comment the previous line and uncomment the next line of code
    #options = webdriver.FirefoxOptions()

    options.add_argument('--start-maximized')
    simple_driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', options=options)

    # To use Firefox driver comment the previous line and uncomment the next line of code
    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    request.cls.simple_driver = simple_driver
    yield
    print('teardown method')
    simple_driver.quit()

@pytest.fixture()
def setup_teardown_shop(request):
    global driver
    simple_driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = EventFiringWebDriver(simple_driver, MyListener())
    request.cls.driver = driver
    yield
    simple_driver.quit()

class MyListener(AbstractEventListener):

    def before_find(self, by, value, driver):
        print(f'Finding element by {by} with value {value}')

    def after_find(self, by, value, driver):
        print(f'Element by {by} with value {value} found.')

    def before_click(self, element, driver):
        print(f'Will click on element with text {element}, its text is {element.text}')

    def after_click(self, element, driver):
        print(f'Successfully clicked on element.')
