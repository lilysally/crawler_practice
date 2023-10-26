from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC

# TypeError: WebDriver.__init__() got an unexpected keyword argument 'executable_path' in Selenium Python
service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
chrome  = webdriver.Chrome(service=service, options=options)

chrome.get("https://www.facebook.com/")
 
email = chrome.find_element(By.ID,"email")
password = chrome.find_element(By.ID,"pass")
 
email.send_keys('youremail')
password.send_keys('yourpassword')
password.submit()

time.sleep(3)

# 處理通知彈出框
try:
    allow_button = chrome.find_element(By.XPATH, "//button[@name='__CONFIRM__']")
    allow_button.click()
except:
    print("通知彈窗未找到或處理失敗")

# 進入目標頁面
chrome.get('https://www.facebook.com/learncodewithmike')

time.sleep(3)

# 關閉瀏覽器
chrome.quit()