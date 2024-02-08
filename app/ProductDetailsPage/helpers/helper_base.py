from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




class HelperFunc(object):
    __TIMEOUT = 10
    basePageURL = "https://equipmentshare.com"
    categoriesPageURL = basePageURL + "/rent-new"

    def __init__(self, driver):
        super(HelperFunc, self).__init__()
        self._driver_wait = WebDriverWait(driver, HelperFunc.__TIMEOUT)
        self._driver = driver
        # set implicit wait time
        driver.implicitly_wait(10)  # seconds

    def open(self, url):
        self._driver.get(url)

    def maximize(self):
        self._driver.maximize_window()
    def refresh(self):
        self._driver.refresh()

    def explicitWait(self, xpath):
        try:
        # wait 10 seconds before looking for element
            element = WebDriverWait(self._driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, xpath))
            )
        finally:
            self._driver.close()
    def close(self):
        self._driver.quit()

    # Helper functions that are used to identify the web locators in Selenium Python tutorial

    def find_by_xpath(self, xpath):
        return self._driver.find_element(By.XPATH, xpath)

    def find_by_name(self, name):
        return self._driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))

    def find_by_id(self, id):
        return self._driver_wait.until(EC.visibility_of_element_located((By.ID, id)))

    def find_page_title(self):
        return self._driver.title

    def find_page_URL(self):
        return self._driver.current_url
