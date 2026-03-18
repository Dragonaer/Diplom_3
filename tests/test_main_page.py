
import allure
from pages.main import MainPage
from locators.main import MainLocators
from locators.login_in import LoginInLocators
from locators.order_feed import OrderFeedLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


from curl import *

class TestMainPage:
    @allure.title("Переход по клику на кнопку Конструктор")
    def test_constructor_button(self, browser_driver):
        page = MainPage(driver=browser_driver)
        page.click_on_element(LoginInLocators.ENTER_BUTTON)
        page.click_on_element(MainLocators.CONSTRUCTOR_BUTTON)
        assert page.url == main_site

    @allure.title("Переход по клику на раздел Лента заказов")
    def test_order_feel_button(self, browser_driver):
        page = MainPage(driver=browser_driver)
        page.click_on_element(OrderFeedLocators.ORDER_FEED_BUTTON)
        assert page.url == order_feed_page

    @allure.title("Появление всплывающего окна при клике на ингредиент")
    def test_information_bread(self, browser_driver):
        page = MainPage(driver=browser_driver)
        page.click_on_element(MainLocators.FIRST_BREAD)
        assert page.wait_for_ingredient_popup(MainLocators.POPUP_FIRST_BREAD).is_displayed()


    @allure.title("Закрыть всплывающее окно кликом на крестик")
    def test_close_the_window(self, browser_driver):
        page = MainPage(driver=browser_driver)
        page.click_on_element(MainLocators.FIRST_BREAD)
        page.click_on_element(MainLocators.CLOSE_THE_WINDOW)
        assert WebDriverWait(page.driver, 10).until(
            EC.invisibility_of_element_located(MainLocators.MODAL_CONTENT_BOX)
        )

    @allure.title("Увеличение счетчика ингридиента придобавлении в заказ")
    def test_ingredient_counter(self, browser_driver):
        page = MainPage(driver=browser_driver)
        page.drag_to_cart(MainLocators.FIRST_BREAD, MainLocators.BURGER_CONSTRUCTOR)

        counter = page.get_text_on_element(MainLocators.FIRST_BREAD_COUNTER)
        assert counter == "2"
