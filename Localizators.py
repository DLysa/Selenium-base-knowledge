import time
from asyncio import timeout

from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import title_contains

driver = webdriver.Chrome()

#driver.get(url='https://helion.pl/')

'''LOKALIZATORY'''
#driver.find_element(By.ID, 'inputSearch')
#driver.find_element(By.LINK_TEXT, 'Kontakt')
#driver.find_element(By.CLASS_NAME, 'title-video')
#driver.find_element(By.CLASS_NAME, 'title-video')
#driver.find_element(By.XPATH, '//*{@id="left-big-col"]/div[]/div[1]/p/span')

#elementy = driver.find_elements(By.TAG_NAME, 'li')
#for e in elementy:
#  print(e.text)

print("Rozpoczynam test nr 1")
print("Otwieram stronę...")
driver.implicitly_wait(3)
driver.get(url='https://helion.pl/')
print("Strona otwarta")
print("Wpisuje w wyszukiwarkę...")
driver.find_element(By.ID, 'inputSearch').send_keys('Selenium' + Keys.ENTER)
print("Wyszukano słowo 'Selenium'")
print("Odnajduje książkę o Pythonie...")
#WebDriverWait(driver, timeout=5).until(lambda x:x.find_element(By.CLASS_NAME, 'pytmie-link'))
WebDriverWait(driver, timeout=5).until(
    title_contains('Szukasz "Selenium"'))
print('Czekam na tytuł - Szukasz "Selenium" ')
chosenBook= WebDriverWait(driver, timeout=5, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException]).until(
   lambda x: x.find_element(By.CLASS_NAME, 'seler2--link.short-title'))
driver.execute_script("arguments[0].click();", chosenBook)
# print("Poszukuje elementu 'vteaue-link'")
# driver.find_element(By.CLASS_NAME, 'vteaue--link.short-title').click()

print("Książka odnaleziona!")
print("Zaglądam do książki...")

zajrzyj = WebDriverWait(driver, timeout=5, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException]).until(
   lambda x: x.find_element(By.ID, 'zajrzyj'))
zajrzyj.click()
# zajrzyj = driver.find_element(By.ID, 'zajrzyj')
#webdriver.ActionChains(driver).click_and_hold(zajrzyj).perform()
#webdriver.ActionChains(driver).context_click(zajrzyj).perform()
time.sleep(10)
print("Test nr 1 wykonany prawidłowo!")
print("KONIEC")
