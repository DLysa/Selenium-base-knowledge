import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://helion.pl")
driver.find_element(By.LINK_TEXT, "Videokursy").click()

driver.back()
time.sleep(3)
driver.forward()
driver.refresh()

driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://python.org")
time.sleep(3)
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
time.sleep(3)
driver.set_window_size(800,600)
time.sleep(3)
driver.maximize_window()

