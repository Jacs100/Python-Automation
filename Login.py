from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

print("Script is started to here............")
driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
clm_app = "http://10.88.152.30:8020/"
driver.get(clm_app)
time.sleep(2)
driver.find_element(by=By.ID, value="Username").send_keys("Jayesh")
time.sleep(2)
driver.find_element(by=By.NAME, value="Password").send_keys("Mantra@123")
time.sleep(5)
driver.find_element(by=By.ID, value="btnSubmit").click()

driver.get("http://10.88.152.30:8020/DashBoard/TimeAttendanceDashBoard")
time.sleep(2)
driver.get("http://10.88.152.30:8020/Leave/LeaveType")
time.sleep(2)
driver.find_element(by=By.ID, value="btnOpenModel").click()
time.sleep(1)
driver.find_element(by=By.ID,value="MastName").send_keys("MK")
time.sleep(1)
driver.find_element(by=By.ID, value="Description").send_keys("Mankel Lal")
time.sleep(1)
driver.find_element(by=By.ID, value="calculatebalance").click()
time.sleep(1)
driver.find_element(by=By.NAME, value="btnsubmit").click()
time.sleep(2)


#time.sleep(2)
#23
print("Your Script is Ending Here..")
driver.close()
