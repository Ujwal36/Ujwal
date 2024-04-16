from selenium.webdriver.support.wait import WebDriverWait

from app.RentalWebAutomationTests.helpers.helper_base import HelperFunc


def __init__(self, driver):
    super(HelperFunc, self).__init__()
    self._driver_wait = WebDriverWait(driver, HelperFunc.TIMEOUT)
    self._driver = driver

