import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = None

@pytest.fixture()
def setup_teardown(request):
    global driver
    print('setup method')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = driver
    yield
    print('teardown method')
    driver.quit()