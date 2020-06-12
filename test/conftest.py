import pytest
from selenium import webdriver

driver = None

@pytest.fixture()
def setup_teardown(request):
    global driver
    print('setup method')
    driver = webdriver.Chrome(executable_path="/home/lpoplavska/Documents/chromedriver")
    request.cls.driver = driver
    yield
    print('teardown method')
    driver.quit()