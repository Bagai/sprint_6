from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_HEADER_ORDER = (
        By.XPATH,
        "//div[contains(@class, 'Header_Nav')]/button[contains(@class, 'Button_Button')]",
    )
    QUESTION_XPATH = (
        By.XPATH,
        '//div[@id="accordion__panel-{}"]',
    )
    ANSWER_XPATH = (
        By.XPATH,
        '//div[@id="accordion__panel-{}"]',
    )
    QUESTION_TO_SCROLL_XPATH = (By.XPATH, "//div[@id='accordion__panel-7']")
