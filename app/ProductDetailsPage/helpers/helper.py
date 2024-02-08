from helpers.helper_base import HelperFunc
from selenium.webdriver import WebDriverWait


def __init__(self, driver):
    super(HelperFunc, self).__init__()
    self._driver_wait = WebDriverWait(driver, HelperFunc.__TIMEOUT)
    self._driver = driver

