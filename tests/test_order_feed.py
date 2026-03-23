import allure
from pages.base_page import *
from locators.main import *
from locators.login_in import *
from pages.main_page import MainPage
from pages.order_feed import OrderFeed

from curl import *


class TestOrderFeed:
    @allure.title(
        "При создании нового заказа счётчик Выполнено за всё время увеличивается"
    )
    def test_ingredient_counter_all_times(self, driver_logged_in):
        list_page = OrderFeed(driver=driver_logged_in)
        order_page = MainPage(driver=driver_logged_in)
        list_page.click_on_order_feed()
        all_time_orders = list_page.get_indications_counter_all_time()
        
        list_page.click_on_constructor()
        order_page.drag_ingredient_to_order()
        order_page.enter_create_button()
        order_page.close_the_window_with_order_id()
        list_page.click_on_order_feed()
        now_order = list_page.get_indications_counter_all_time()
        assert all_time_orders < now_order

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


    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_id_order_in_work(self, driver_logged_in):
        list_page = OrderFeed(driver=driver_logged_in)
        order_page = MainPage(driver=driver_logged_in)
        list_page.click_on_constructor()
        order_page.drag_ingredient_to_order()
        order_page.enter_create_button()
        order_ID = order_page.get_order_id()
        order_page.close_the_window_with_order_id()
        list_page.click_on_order_feed()
        
        assert list_page.id_order_in_progress(order_ID)






