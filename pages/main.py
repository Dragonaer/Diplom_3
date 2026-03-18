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
    def drag_to_cart(self, locator1, locator2):
        source = self.driver.find_element(*locator1)
        target = self.driver.find_element(*locator2)
        actions = ActionChains(self.driver)
        actions.click_and_hold(source).pause(0.5)
        actions.move_to_element(target).pause(0.5)
        actions.release().pause(0.5)
        actions.perform()

    @allure.step("Обновление страницы")
    def refresh(self):
        self.driver.refresh()

    @allure.step("Подождать модельное окно")
    def wait_for_modal_window(self, locator):
        self.wait_for_element(locator)

    @allure.step(
        "Подождать прогрузки модельного окна"
    )
    def get_order_id(self, locator, max_id):
        self.wait.until_not(
            EC.text_to_be_present_in_element(locator, max_id) 
        )
        return self.get_text_on_element(locator)
