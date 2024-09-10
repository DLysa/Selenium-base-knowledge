from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.google.com")

driver.find_element(By.ID, "L2AGLb").click()
gmail = driver.find_element(By.LINK_TEXT, "Gmail")
webdriver.ActionChains(driver).move_to_element(gmail).perform()

x = 100
y = 100

webdriver.ActionChains(driver).move_by_offset(x,y).perform()