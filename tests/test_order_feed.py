import allure
from pages.base_page import *
from locators.main import *
from locators.login_in import *
from locators.order_feed import OrderFeedLocators
from pages.main_page import MainPage
from pages.order_feed import OrderFeed

from curl import *


class TestOrderFeed:
    # @allure.title(
    #     "При создании нового заказа счётчик Выполнено за всё время увеличивается"
    # )
    # def test_ingredient_counter_all_times(self, driver_logged_in):
    #     list_page = OrderFeed(driver=driver_logged_in)
    #     order_page = MainPage(driver=driver_logged_in)
    #     list_page.click_on_order_feed()
    #     all_time_orders = list_page.get_indications_counter_all_time()
        
    #     list_page.click_on_constructor()
    #     order_page.drag_ingredient_to_order()
    #     order_page.enter_create_button()
    #     order_page.close_the_window_with_order_id()
    #     list_page.click_on_order_feed()
    #     now_order = list_page.get_indications_counter_all_time()
    #     assert all_time_orders < now_order

    @allure.title("При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_ingredient_counter_all_day(self, driver_logged_in):
        list_page = OrderFeed(driver=driver_logged_in)
        order_page = MainPage(driver=driver_logged_in)
        list_page.click_on_order_feed()
        today_orders = list_page.get_indications_counter_today()
        
        list_page.click_on_constructor()
        order_page.drag_ingredient_to_order()
        order_page.enter_create_button()
        order_page.close_the_window_with_order_id()
        list_page.click_on_order_feed()
        now_order = list_page.get_indications_counter_today()
        assert today_orders < now_order

    # @allure.title("После оформления заказа его номер появляется в разделе В работе")
    # def test_id_order_in_work(self, driver_logged_in, driver_feed_page):
    #     list_page = BasePage(driver=driver_feed_page)
    #     order_page = BasePage(driver=driver_logged_in)
    #     order_page.drag_to_cart(MainLocators.FIRST_BREAD, MainLocators.BURGER_CONSTRUCTOR)
    #     order_page.click_on_element(MainLocators.CREATE_ORDER_BUTTON)
    #     order_page.wait_for_modal_window(MainLocators.MODAL_CONTENT_BOX)
    #     list_page.refresh()
    #     in_progress_orders = list_page.get_text_on_element(
    #         OrderFeedLocators.IN_PROGRESS_ORDERS
    #     )
    #     order_id = order_page.get_order_id(MainLocators.MODAL_CONTENT_BOX, "9999")
    #     order_id = order_id.split()[0]
    #     order_id = (7 - len(order_id)) * "0" + order_id
    #     assert order_id == in_progress_orders
