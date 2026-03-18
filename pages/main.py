import time

import allure
from locators.main import MainLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


TIMEOUT = 10


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.wait.until(EC.invisibility_of_element_located(MainLocators.MODAL_OVERLAY))

    @property
    def url(self):
        return self.driver.current_url

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step("Ввести текст элемента")
    def send_keys_to_input(self, locator, keys, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step("Перетащить ингредиент в корзину")
    def drag_to_cart(self, locator):
        source = self.driver.find_element(*locator)
        target = self.driver.find_element(*MainLocators.BURGER_CONSTRUCTOR)
        actions = ActionChains(self.driver)
        actions.click_and_hold(source).pause(0.5)
        actions.move_to_element(target).pause(0.5)
        actions.release().pause(0.5)
        actions.perform()

    @allure.step("Обновление страницы")
    def refresh(self):
        self.driver.refresh()

    @allure.step("Подождать модельное окно")
    def wait_for_modal_window(self):
        self.wait_for_element(MainLocators.MODAL_CONTENT_BOX)

    @allure.step(
        "Подождать прогрузки модельного окна, чтобы не отображался номер заказа 9999"
    )
    def get_order_id(self):
        self.wait.until_not(
            EC.text_to_be_present_in_element(MainLocators.MODAL_CONTENT_BOX, "9999")
        )
        return self.get_text_on_element(MainLocators.MODAL_CONTENT_BOX)
