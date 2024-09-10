import unittest
from selenium import webdriver
import page


class PythonSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")

    def test_search_python_org(self):
        main_page = page.MainPage(self.driver)
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_result_found(),"Nie odnaleziono"

    def tearDown(self):
        self.driver.close()