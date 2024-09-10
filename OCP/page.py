from element import BasePageElement
from locators import MainPageLocators

class SearchTextElement(BasePageElement):
    locator = 'q'

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        self.driver.find_element(*MainPageLocators.GO_BUTTON).click()

class SearchResultPage(BasePage):
    def is_result_found(self):
        return "Nie odnaleziono" not in self.driver.page_source