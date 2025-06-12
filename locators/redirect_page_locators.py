from selenium.webdriver.common.by import By


class RedirectPageLocators:
    LOGO_YANDEX_XPATH = (By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]")
    LOGO_SCOOTER_XPATH = (By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]")
    IMG_SCOOTER_XPATH = (By.XPATH, ".//img[@alt='Scooter blueprint']")
    BUTTON_DZEN_FIND_XPATH = (By.XPATH, ".//button[contains(@class, 'arrow__button') and text()='Найти']")
