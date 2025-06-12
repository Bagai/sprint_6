from selenium.webdriver.firefox.options import Options

from selenium import webdriver
import pytest


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920x1080")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()
