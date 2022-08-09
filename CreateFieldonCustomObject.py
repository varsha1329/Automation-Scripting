from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
option1 =Options()
option1.add_argument("--disable-notificatios")


driver = webdriver.Chrome(executable_path="C:\Program Files\Python310\ChromeWebdriver\chromedriver.exe",chrome_options=option1);
driver.maximize_window()
driver.get("https://login.salesforce.com/");
driver.find_element(By.ID,'username').send_keys('automationvarsha12@gmail.com')
driver.find_element(By.ID,'password').send_keys('Auto@123')
driver.find_element(By.ID,"Login").click()
driver.find_element(By.CLASS_NAME,"switch-to-lightning").click()
driver.find_element(By.LINK_TEXT,"Object Manager").clicl()
driver.find_element(By.ID,'globalQuickfind').send_keys('Custome12')
driver.find_element(By.LINK_TEXT,"Custome12").click()
driver.find_element(By.LINK_TEXT,"Fields & Relationships").click()
driver.find_element(By.CLASS_NAME,"slds-button slds-button--neutral uiButton").click()
driver.find_element(By.ID,'dtypeX').click()
driver.find_element(By.NAME,"goNext").click()
driver.find_element(By.ID,'MasterLabel').send_keys("Name Of Customer")
driver.find_element(By.NAME,"goNext").click()
driver.find_element(By.NAME,"goNext").click()
driver.find_element(By.XPATH,('//*[@id="stageForm"]/div/div[2]/div[1]/div/input[3]')).click()