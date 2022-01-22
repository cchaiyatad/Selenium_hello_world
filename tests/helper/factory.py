from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

def new_driver(browser, options = None):
    if browser == "chrome":
        service = ChromeService(executable_path=ChromeDriverManager().install())
        if options == None:
            options = ChromeOptions()
        return webdriver.Chrome(service=service, options=options)
    if browser == "firefox":
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        if options == None:
            options = FirefoxOptions()
        return webdriver.Firefox(service=service, options=options)
    if browser == "safari":
        return webdriver.Safari()
