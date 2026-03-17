import allure
from pages.main_page import *
from locators.main_page import *
from locators.login_in import *
from locators.order_feed import OrderFeedLocators
from pages.main_page import BasePage
from curl import *


class TestMainPage:
    @allure.title("Переход по клику на кнопку Конструктор")
    def test_constructor_button(self, browser_driver):
        page = BasePage(driver=browser_driver)
        page.click_on_element(LoginInLocators.ENTER_BUTTON)
        page.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

        assert page.url == main_site

    @allure.title("Переход по клику на раздел Лента заказов")
    def test_order_feel_button(self, browser_driver):
        page = BasePage(driver=browser_driver)
        page.click_on_element(OrderFeedLocators.ORDER_FEED_BUTTON)

        assert page.url == order_feed_page

    @allure.title("Появление всплывающего окна при клике на ингридиент")
    def test_information_bread(self, browser_driver):
        page = BasePage(driver=browser_driver)
        page.click_on_element(MainPageLocators.FIRST_BREAD)
        counter = page.get_text_on_element(MainPageLocators.NAME_FIRST_BREAD)
        
        assert counter == "Флюоресцентная булка R2-D3"

    @allure.title("Закрыть всплывающее окна кликом на крестик")
    def test_close_the_window(self, browser_driver):
        page = BasePage(driver=browser_driver)
        page.click_on_element(MainPageLocators.FIRST_BREAD)
        page.click_on_element(MainPageLocators.CLOSE_THE_WINDOW)
        counter = page.get_text_on_element(MainPageLocators.TEXT_FILLING_BUTTON)
        
        assert counter == "Начинки"

    @allure.title("Увеличение счетчика ингридиента придобавлении в заказ")
    def test_ingredient_counter(self, browser_driver):
        page = BasePage(driver=browser_driver)
        page.drag_to_cart(MainPageLocators.FIRST_BREAD)
        
        counter = page.get_text_on_element(MainPageLocators.FIRST_BREAD_COUNTER)
        assert counter == "2"

    



