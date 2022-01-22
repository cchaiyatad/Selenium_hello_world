import pytest

from selenium import webdriver

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver.common.by import By

def test_firefox_session():
    service = FirefoxService(executable_path=GeckoDriverManager().install())
    options = FirefoxOptions()
    driver = webdriver.Firefox(service=service, options=options)

    driver.get("https://google.com")

    assert driver.title == "Google"

    driver.implicitly_wait(0.5)

    search_box = driver.find_element(by=By.NAME, value="q")
    search_button = driver.find_element(by=By.NAME, value="btnK")

    search_box.send_keys("Selenium")
    search_button.click()

    search_box = driver.find_element(by=By.NAME, value="q")
    assert search_box.get_attribute("value") == "Selenium"

    driver.quit()


if __name__ == "__main__":
    test_firefox_session()