import time

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')


@pytest.fixture(scope='function', autouse=True)
def setup(request):
    try:

        browser = request.config.getoption('--browser')
        if browser == 'chrome':
            driver = webdriver.Chrome(executable_path='c:/Drivers/chromedriver.exe')
            driver.get('http://www.moat.com')

        elif browser == 'firefox':
            driver = webdriver.Firefox(executable_path='c:/Drivers/geckodriver.exe')
            driver.get('http://www.moat.com')

        driver.maximize_window()
        driver.implicitly_wait(10)
        request.cls.driver = driver
        time.sleep(3)
        request.addfinalizer(driver.quit)
        # yield
        # driver.close()
        # driver.quit()

    except:
        print('Error at Conftest File')
