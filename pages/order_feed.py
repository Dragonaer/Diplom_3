import allure
from locators.main import MainLocators
from locators.login_in import LoginInLocators
from locators.order_feed import OrderFeedLocators

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


TIMEOUT = 10


class OrderFeed(BasePage):
    
    @allure.step("Кликнуть на кнопку Лента заказа")
    def click_on_order_feed(self):
        self.click_on_element(OrderFeedLocators.ORDER_FEED_BUTTON)