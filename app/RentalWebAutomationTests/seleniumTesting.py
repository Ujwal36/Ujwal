from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com")
driver.maximize_window()

current_title = driver.title
actual_title = "Google"

assert current_title == actual_title
driver.close()
