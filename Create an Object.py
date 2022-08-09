from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Program Files\Python310\ChromeWebdriver\chromedriver.exe");
driver.maximize_window()
driver.get("https://login.salesforce.com/");
driver.find_element(By.ID,'username').send_keys('automationvarsha12@gmail.com')
driver.find_element(By.ID,'password').send_keys('Auto@123')
driver.find_element(By.ID,"Login").click()
#driver.find_element(By.CLASS_NAME,"switch-to-lightning").click()


#driver.find_element(By.ID,'setupSearch').send_keys("object")
driver.find_element(By.LINK_TEXT,'New custom object').click()
driver.find_element(By.ID,'MasterLabel').send_keys("Custome12")
driver.find_element(By.ID,'PluralLabel').send_Keys("Custome12")
driver.find_element(By.NAME,"save").click()
