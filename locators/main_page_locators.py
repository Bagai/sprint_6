from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_HEADER_ORDER = (
        By.XPATH,
        ".//div[contains(@class, 'Header_Nav')]/button[contains(@class, 'Button_Button')]",
    )
    BUTTON_FOOTER_ORDER = (
        By.XPATH,
        ".//div[contains(@class, 'Home_FinishButton')]/button[contains(@class, 'Button_UltraBig') and text()='Заказать']",
    )
    QUESTION_XPATH = (
        By.XPATH,
        './/div[@id="accordion__heading-{}"]',
    )
    ANSWER_XPATH = (
        By.XPATH,
        './/div[@id="accordion__panel-{}"]',
    )
    QUESTION_TO_SCROLL_XPATH = (By.XPATH, ".//div[@id='accordion__heading-7']")
