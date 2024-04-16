from helpers.helper_base import HelperFunc
from selenium import webdriver


def get_browser(browser):
    if browser == "chrome":
        return HelperFunc(webdriver.Chrome())
    elif browser == "firefox":
        return HelperFunc(webdriver.Firefox())
    elif browser == "safari":
        return HelperFunc(webdriver.Safari())

