import os
import sys

script_dir = os.path.dirname( __file__ )
helper_dir = os.path.join( script_dir, '..', 'helper' )
sys.path.append( helper_dir )
import factory

import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_open_tab():
    drivers = [factory.new_driver("chrome"), factory.new_driver("safari")]
    for driver in drivers:
        do_test_open_tab(driver)
        
def do_test_open_tab(driver):
    driver.get("https://seleniumhq.github.io")
    assert driver.title == "Selenium"

    wait = WebDriverWait(driver, 10)

    first_window = driver.current_window_handle

    assert len(driver.window_handles) == 1

    driver.switch_to.new_window('tab')
    wait.until(EC.number_of_windows_to_be(2))
    
    time.sleep(3)
    driver.get("https://www.google.com")
    second_window = driver.current_window_handle
    assert driver.title == "Google"
    
    time.sleep(3)
    driver.switch_to.window(first_window)
    assert driver.title == "Selenium"
    time.sleep(3)

    driver.close()
    driver.switch_to.window(second_window)
    time.sleep(3)
    assert driver.title == "Google"

    time.sleep(3)
    driver.quit()



if __name__ == "__main__":
    test_open_tab()