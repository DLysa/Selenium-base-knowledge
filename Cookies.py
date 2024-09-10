from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://helion.pl")

# driver.add_cookie({"name":"dominik","value":"selenium"})
driver.delete_cookie("dominik")

print(driver.get_cookies())