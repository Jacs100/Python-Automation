import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#
#driver = webdriver.Chrome(r"C:\Users\Jayesh.Marvadi\PycharmProjects\SeleniumTest\Browsers\")
driver = webdriver.Chrome(r"/Browsers/chromedriver.exe")
driver.maximize_window()
driver.get('https://www.google.com/')
print("Script started for run")
#driver.find_element_by_name("q").send_keys("javapoint")
driver.find_element(by=By.NAME, value="q").send_keys("javapoint")
time.sleep(5)

#driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
driver.find_element(by=By.NAME, value="btnK").send_keys(Keys.ENTER)
time.sleep(5)
driver.close()
print("Your Script is runnig sucessfully")
# Zzxzx








