from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Program Files\Python310\ChromeWebdriver\chromedriver.exe");
driver.maximize_window()
driver.get("https://login.salesforce.com/")

driver.find_element(By.ID,'username').send_keys('tatatesting@360dc.com')

driver.find_element(By.ID,'password').send_keys('Varsha@G123')

#driver.find_element_by_xpath("//*[@id='username']").send_keys('tatatesting@360dc.com')
#find_element(By.XPATH,(‘//*[@id='username']").send_keys('tatatesting@360dc.com’)
#driver.find_element_by_xpath("//*[@id='password']").send_Keys('Varsha@G123')
#driver.find_element_by_xpath("//*[@id='Login']").click()
driver.find_element(By.ID,"Login").click()