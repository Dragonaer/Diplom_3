from selenium.webdriver.common.by import By


class OrderFeedLocators:

    ORDER_FEED_BUTTON = (By.XPATH,'(//p[@class="AppHeader_header__linkText__3q_va ml-2"])[2]',)  # кнопка Лента заказов
    ALL_ORDERS = (By.XPATH, "//p[contains(text(),'Выполнено за все время:')]/following-sibling::p") # счетчик «Выполнено за все время»
    ORDERS_TODAY = (By.XPATH,"//p[contains(text(),'Выполнено за сегодня:')]/following-sibling::p") # счетчи «Выполнено за сегодня»
    IN_PROGRESS_ORDERS = (By.XPATH,'//*[@id="root"]/div/main/div/div/div/div[1]/ul[2]/li') # раздел В работе
