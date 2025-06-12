from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT_XPATH = (
        By.XPATH,
        ".//input[@placeholder='* Имя']",
    )
    SURNAME_INPUT_XPATH = (
        By.XPATH,
        ".//input[@placeholder='* Фамилия']",
    )
    ADDRESS_INPUT_XPATH = (
        By.XPATH,
        ".//input[@placeholder='* Адрес: куда привезти заказ']",
    )
    PHONE_INPUT_XPATH = (
        By.XPATH,
        ".//input[@placeholder='* Телефон: на него позвонит курьер']",
    )
    DATE_XPATH = (
        By.XPATH,
        ".//input[@placeholder='* Когда привезти самокат']",
    )
    DATE_CLICK_XPATH = (
        By.XPATH,
        ".//div[text()='13']",
    )
    METRO_STATION_XPATH = (
        By.XPATH,
        ".//div[text()='Бульвар Рокоссовского']",
    )
    INPUT_METRO_STATION_XPATH = (
        By.XPATH,
        ".//input[@placeholder='* Станция метро']",
    )
    DURATION_XPATH = (
        By.XPATH,
        ".//div[text()='* Срок аренды']",
    )
    SET_DURATION_XPATH = (
        By.XPATH,
        ".//div[text()='двое суток']",
    )
    COLOR_XPATH = (
        By.XPATH,
        ".//input[@id='black']",
    )
    COMMENT_XPATH = (
        By.XPATH,
        ".//input[@placeholder='Комментарий для курьера']",
    )
    NEXT_ORDER_BUTTON_XPATH = (
        By.XPATH,
        ".//button[contains(@class, 'Button_Middle') and text()='Далее']",
    )
    ORDER_BUTTON_XPATH = (
        By.XPATH,
        ".//button[contains(@class, 'Button_Middle') and text()='Заказать']",
    )
    CONFIRM_ORDER_BUTTON_XPATH = (
        By.XPATH,
        ".//button[contains(@class, 'Button_Middle') and text()='Да']",
    )
    CONFIRMATION_MODAL_XPATH = (
        By.XPATH,
        ".//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]",
    )
