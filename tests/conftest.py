import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from curl import *
from data import *
from locators.login_in import LoginInLocators


BASE_OPTIONS_CHROME = ChromeOptions()
BASE_OPTIONS_CHROME.add_argument("--window-size=1200,800")
BASE_OPTIONS_CHROME.add_argument("--headless")

BASE_OPTIONS_FF = FirefoxOptions()
BASE_OPTIONS_FF.add_argument("--window-size=1200,800")
BASE_OPTIONS_FF.add_argument("--headless")


@pytest.fixture(params=["chrome","firefox"])
def browser_driver(request):
    browser_name = request.param
    if browser_name == "chrome":
        driver = webdriver.Chrome(options=BASE_OPTIONS_CHROME)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(options=BASE_OPTIONS_FF)
    driver.get(main_site)
    yield driver
    driver.quit()


@pytest.fixture
def driver_logged_in(browser_driver):
    driver = browser_driver
    driver.get(login_page)
    driver.find_element(*LoginInLocators.EMAIL).send_keys(Credentials.email)
    driver.find_element(*LoginInLocators.PASSWORD).send_keys(Credentials.password)
    driver.find_element(*LoginInLocators.SIGN_IN_BUTTON).click()
    yield driver


@pytest.fixture
def driver_feed_page(browser_driver):
    driver = browser_driver
    driver.get(order_feed_page)
    yield driver

