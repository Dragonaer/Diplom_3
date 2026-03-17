from selenium.webdriver.common.by import By


class LoginInLocators:
    # локаторы для входа
    ENTER_BUTTON = (
        By.XPATH,
        '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]',
    )  # кнопка "ВОЙТИ В АККАУНТ" на главной странице
   
    EMAIL = (
        By.XPATH,
        '//input[@name="name"]',
    )  # поле ввода email

    PASSWORD = (
        By.XPATH,
        '//input[@type="password"]',
    )  # поле ввода пароля

    SIGN_IN_BUTTON = (
        By.XPATH,
        '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]',
    )  # кнопка "ВОЙТИ" после ввода данных

