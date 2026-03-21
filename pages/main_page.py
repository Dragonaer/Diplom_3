import allure
from locators.main import MainLocators
from locators.login_in import LoginInLocators

from pages.base_page import BasePage


TIMEOUT = 10


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Кликнуть на кнопку Входа")
    def click_on_enter_button(self):
        self.click_on_element(LoginInLocators.ENTER_BUTTON)
    
    @allure.step("Кликнуть на Конструктор")
    def click_on_constructor(self):
        self.click_on_element(MainLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на первую позицию (хлеб) в конструкоторе заказа")
    def click_on_first_bread(self):
        self.click_on_element(MainLocators.FIRST_BREAD)

    @allure.step("Отображение попапа с первой позицией (хлебом) в конструкторе заказа")
    def popup_with_first_bread(self):
        self.wait_for_ingredient_popup(MainLocators.POPUP_FIRST_BREAD)
        return self.wait_for_element(MainLocators.POPUP_FIRST_BREAD)

    @allure.step("Отображение попапа с первой позицией (хлебом) в конструкторе заказа")
    def close_the_window_ingregient(self):
        self.click_on_element(MainLocators.CLOSE_THE_WINDOW)

    @allure.step("Перетаскивание ингридиента в корзину")
    def drag_ingredient_to_order(self):
        self.drag_to_cart(MainLocators.FIRST_BREAD, MainLocators.BURGER_CONSTRUCTOR)

    @allure.step("Получение количества ингредиентов у позиции")
    def counter_ingredient(self):
        return self.find_element(MainLocators.FIRST_BREAD_COUNTER).text
    
    @allure.step("Начажать кнопку Сделать заказ")
    def enter_create_button(self):
        self.click_on_element(MainLocators.CREATE_ORDER_BUTTON)
        
    @allure.step("Подождать модельное окно с номером заказа")
    def wait_for_modal_window_with_order_ID(self):
        self.wait_for_element(MainLocators.MODAL_CONTENT_BOX)

    
    @allure.step("Закрыть модельное окно с номером заказа")
    def close_the_window_with_order_id(self):
        self.loading_modal_window(MainLocators.MODAL_CONTENT_BOX, '9999')
        self.click_on_element(MainLocators.CLOSE_THE_WINDOW_WITH_ORDER_ID)

    @allure.step("Получить номер заказа")
    def get_order_id(self):
        element = self.wait_for_element(MainLocators.ORDER_ID)
        number_text = element.text
        if number_text == "9999":
            self.loading_modal_window(MainLocators.ORDER_ID, "9999")
            element = self.wait_for_element(MainLocators.ORDER_ID)
            number_text = element.text

        return number_text