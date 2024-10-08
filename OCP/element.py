from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object):
    def __set__(self, obj, value):

        driver = obj.driver
        WebDriverWait(driver, 10).until(
            lambda driver:driver.find_element(By.NAME, self.locator))
        driver.find_element(By.NAME, self.locator).clear().send_keys(value)

    def __get__(self,obj,owner):
        driver = obj.driver
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element(By.NAME, self.locator))
        element = driver.find_element(By.NAME, self.locator)
        return element.get_attribute('value')