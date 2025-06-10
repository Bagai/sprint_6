from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def click_element(self, locator):
        self.wait.until(ex.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).click()

    def find_element_with_wait(self, locator):
        self.wait.until(ex.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def format_locator(self, locator, num_of_qa):
        method, unpack_locator = locator
        return (method, unpack_locator.format(num_of_qa))

    def get_element_text(self, locator):
        return self.find_element_with_wait(locator).text

    def scroll_to_element(self, locator):
        self.driver.execute_script(
            "arguments[0].scrollIntoView();", self.find_element_with_wait(locator)
        )
