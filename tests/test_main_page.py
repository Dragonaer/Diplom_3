
import allure
from pages.main_page import MainPage
from pages.order_feed import OrderFeed

from locators.main import MainLocators

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


from curl import *

class TestMainPage:
    @allure.title("Переход по клику на кнопку Конструктор")
    def test_constructor_button(self, browser_driver):
        page = MainPage(driver=browser_driver)
        page.click_on_enter_button()
        page.click_on_constructor()
        assert page.url == main_site

    @allure.title("Переход по клику на раздел Лента заказов")
    def test_order_feel_button(self, browser_driver):
        page = OrderFeed(driver=browser_driver)
        page.click_on_order_feed()
        assert page.url == order_feed_page

    @allure.title("Появление всплывающего окна при клике на ингредиент")
    def test_information_bread(self, browser_driver):
        page = MainPage(driver=browser_driver)
        page.click_on_first_bread()
        assert page.popup_with_first_bread().is_displayed()


    @allure.title("Закрыть всплывающее окно кликом на крестик")
    def test_close_the_window(self, browser_driver):
        page = MainPage(driver=browser_driver)
        page.click_on_first_bread()
        page.close_the_window_ingregient()
        assert WebDriverWait(page.driver, 10).until(
            EC.invisibility_of_element_located(MainLocators.MODAL_CONTENT_BOX)
        )

    @allure.title("Увеличение счетчика ингридиента при добавлении в заказ")
    def test_ingredient_counter(self, browser_driver):
        page = MainPage(driver=browser_driver)
        page.drag_ingredient_to_order()
        counter = page.counter_ingredient()
        assert counter == "2"
