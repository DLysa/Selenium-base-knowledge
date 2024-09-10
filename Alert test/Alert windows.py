from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.get('C:/alerty.html')

# okienko alert
# driver.find_element(By.LINK_TEXT, "Kliknij, aby wyświetlić okienko alert").click()

# alert = WebDriverWait(driver, timeout=15).until(expected_conditions.alert_is_present())
# text = alert.text
# alert.accept()

# okienko confirm (odrzuć)
# driver.find_element(By.LINK_TEXT, "Kliknij, aby wyświetlić okienko confirm").click()
# WebDriverWait(driver, timeout=15).until(expected_conditions.alert_is_present())
# alert = driver.switch_to.alert
# text = alert.text
#
# alert.dismiss()

#okienko prompt
driver.find_element(By.LINK_TEXT, "Kliknij, aby wyświetlić okienko prompt").click()

WebDriverWait(driver, timeout=15).until(expected_conditions.alert_is_present())

alert = Alert(driver)

alert.send_keys("Selenium!")

alert.accept()



