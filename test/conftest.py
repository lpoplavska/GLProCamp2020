import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = None

@pytest.fixture()
def setup_teardown_browserstack(request):
    """
    Fixture to setup webdriver using browserstack
    :param request:
    :return:
    """
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

@pytest.fixture()
def setup_teardown_local(request):
    """
    Fixture to setup webdriver location as project directory
    :param request:
    :return:
    """
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield
    print('teardown method')
    driver.quit()

@pytest.fixture()
def setup_teardown_wd_manager(request):
    """
    Fixture to setup webdriver by webdriver manager
    :param request:
    :return:
    """
    global driver
    options = webdriver.ChromeOptions()

    #To initialize Firefox driver comment the previous line and uncomment the next line of code
    #options = webdriver.FirefoxOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # To use Firefox driver comment the previous line and uncomment the next line of code
    #driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    request.cls.driver = driver
    yield
    print('teardown method')
    driver.quit()

@pytest.fixture()
def setup_teardown_selenium_server(request):
    """
    Fixture to setup webdriver by selenium server (Grid)
    :param request:
    :return:
    """
    global driver
    options = webdriver.ChromeOptions()

    #To initialize Firefox driver comment the previous line and uncomment the next line of code
    #options = webdriver.FirefoxOptions()

    options.add_argument('--start-maximized')
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', options=options)

    # To use Firefox driver comment the previous line and uncomment the next line of code
    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    request.cls.driver = driver
    yield
    print('teardown method')
    driver.quit()