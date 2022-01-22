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


def test_local_storage_diff_window():
    # not work on safari, WebDirver open private mode that doesn't share localStorage
    drivers = [factory.new_driver("safari")]
    for driver in drivers:
        do_test_local_storage_diff_window(driver)
        
def do_test_local_storage_diff_window(driver):
    driver.get("https://seleniumhq.github.io")
    
    wait = WebDriverWait(driver, 10)
    
    assert driver.execute_script("return window.localStorage.getItem('key-test');") == None
    driver.execute_script("window.localStorage.setItem('key-test', 'value');")
    assert driver.execute_script("return window.localStorage.getItem('key-test');") == 'value'

    first_window = driver.current_window_handle

    assert len(driver.window_handles) == 1
    driver.switch_to.new_window('window')
    wait.until(EC.number_of_windows_to_be(2))
    
    driver.get("https://seleniumhq.github.io")
    second_window = driver.current_window_handle
    
    assert driver.execute_script("return window.localStorage.getItem('key-test');") == 'value'
   
    driver.quit()



if __name__ == "__main__":
    test_local_storage_diff_window()