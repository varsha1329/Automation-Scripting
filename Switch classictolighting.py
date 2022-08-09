from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Program Files\Python310\ChromeWebdriver\chromedriver.exe");
driver.maximize_window()
driver.get("https://login.salesforce.com/")

driver.find_element(By.ID,'username').send_keys('tatatesting@360dc.com')

driver.find_element(By.ID,'password').send_keys('Varsha@G123')
driver.find_element(By.ID,"Login").click()

driver.find_Element(By.xpath("//*[@id='phHeader']/tbody/tr/td[3]/div/div[3]/div/a[1]")).click()