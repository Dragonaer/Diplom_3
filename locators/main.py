from selenium.webdriver.common.by import By


class MainLocators:

    MODAL_OVERLAY = (By.CLASS_NAME,"Modal_modal_overlay__x2ZCr",)  
    # модельное окно, отображающееся на сайте при загрузке страницы
    CONSTRUCTOR_BUTTON = (By.XPATH,'(//p[@class="AppHeader_header__linkText__3q_va ml-2"])[1]',)  
    # кнопка Конструктор
    FIRST_BREAD = (By.XPATH,'//img[@alt="Флюоресцентная булка R2-D3"]',)  
    # первая булка из списка
    NAME_FIRST_BREAD = (By.XPATH,'//p[@class="text text_type_main-medium mb-8"]',)
    FIRST_SAUCE = (By.XPATH,'//img[@alt="Соус Spicy-X"]',)  
    # первый соус из списка
    CLOSE_THE_WINDOW = (By.XPATH,'//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]',)  
    # закрывает окно с выбранной позицией
    TEXT_FILLING_BUTTON = (By.XPATH,'//span[contains(text(), "Начинки")]',)  
    # текст кнопки "Начинки"
    BURGER_CONSTRUCTOR = (By.CLASS_NAME,"BurgerConstructor_basket__list__l9dp_",) 
    # корзина с бургером
    FIRST_BREAD_COUNTER = (By.XPATH,'//p[contains(@class,"counter_counter__num")]',)  
    # счётчик первой булки из списка
    ORDER_ID = (By.XPATH, '//*[@id="root"]/div/section/div[1]/div/h2')  
    # номер заказа
    CREATE_ORDER_BUTTON = (By.XPATH,'//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]',)  
    # кнопка "Оформить заказ"
    MODAL_CONTENT_BOX = (By.XPATH,'//div[@class="Modal_modal__contentBox__sCy8X pt-30 pb-30"]',) 
     # модельное окно при заказе
    CLOSE_THE_WINDOW_WITH_ORDER_ID = (By.XPATH, '//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    # закрыть всплывающее окно с номером заказа
    POPUP_FIRST_BREAD = (By.XPATH, "//img[@src='https://code.s3.yandex.net/react/code/bun-01.png']") 
    # всплывающее окно