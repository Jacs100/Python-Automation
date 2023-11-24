from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
print("TestCase Started")
#driver = webdriver.Chrome()
driver = webdriver.Chrome()
#driver.maximize_window()
# driver.get("www.google.com")
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.gmail.com")
driver.find_element(by=By.ID, value="identifierId").send_keys("earningtricks199@gmail.com")
time.sleep(2)
#driver.find_element_by_xpath("//span[@class='RveJvd snByac'][1]").click()
#using with enter key
# driver.find_element(by=By.XPATH, value="//span[@class='RveJvd snByac'][1]").send_keys(Keys.ENTER)
#  Using with the click event
driver.find_element(by=By.CLASS_NAME, value="VfPpkd-vQzf8d").click()
time.sleep(2)
driver.find_element(by=By.NAME, value="password").send_keys("--your Passowrd")
driver.find_element(by=By.XPATH, value="//span[contains(text(),'Next')][1]").click()
driver.close()
print("Gmail Login Has Been Successfully Completed")
