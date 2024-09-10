from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://helion.pl/')

search = driver.find_element(By.ID, 'inputSearch')
# webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()
action = webdriver.ActionChains(driver)

action.key_down(Keys.SHIFT).send_keys_to_element(search, 'python').key_up(Keys.SHIFT).send_keys('python').perform()
search.clear()