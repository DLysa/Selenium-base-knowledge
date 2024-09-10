from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://www.python.org")

driver.maximize_window()

codeLocalization = driver.find_element(By.CLASS_NAME, 'slide-code')

codeLocalization.screenshot("code.png")

