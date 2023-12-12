
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.rcvacademy.com")
driver.maximize_window()
driver.implicitly_wait(100.3)
print(driver.title)
driver.quit()