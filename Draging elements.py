from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://crossbrowsertesting.github.io/drag-and-drop")

source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

# targetX = target.location.get("x")
# targetY = target.location.get("y")
#
# # webdriver.ActionChains(driver).drag_and_drop(source,target).perform()
# webdriver.ActionChains(driver).drag_and_drop_by_offset(source, targetX, targetY).perform()
webdriver.ActionChains(driver).click_and_hold(source).move_to_element(target).perform()
