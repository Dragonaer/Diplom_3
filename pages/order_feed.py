import allure
from locators.main import MainLocators
from locators.order_feed import OrderFeedLocators
from pages.base_page import BasePage



class OrderFeed(BasePage):
    
    @allure.step("Кликнуть на кнопку Лента заказа")
    def click_on_order_feed(self):
        self.click_on_element(OrderFeedLocators.ORDER_FEED_BUTTON)

    @allure.step("Получить показанние счетчика за всe время")
    def get_indications_counter_all_time(self):
        return int(self.wait_for_element(OrderFeedLocators.ALL_ORDERS).text)
        
    @allure.step("Получить показанние счетчика за сегодня")
    def get_indications_counter_today(self):
        return int(self.wait_for_element(OrderFeedLocators.ORDERS_TODAY).text)
    
    @allure.step("Посмотреть номер заказа в разделе 'В работе'")
    def id_order_in_progress(self, order_ID):
        return self.wait_text_in_elements(OrderFeedLocators.IN_PROGRESS_ORDERS, order_ID)

    @allure.step("Кликнуть на Конструктор")
    def click_on_constructor(self):
        self.click_on_element(MainLocators.CONSTRUCTOR_BUTTON)