from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Program Files\Python310\ChromeWebdriver\chromedriver.exe");
driver.maximize_window()
driver.get("https://login.salesforce.com/")

driver.find_element(By.ID,'username').send_keys('tatatesting@360.com')

driver.find_element(By.ID,'password').send_keys('Varsh@G123')

driver.find_element(By.ID,"Login").click()
driver.find_element(By.ID,"Error").get.Text();
driver.quite();
