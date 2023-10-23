from selenium import webdriver
from selenium.webdriver.common.by import By

# 初始化瀏覽器
driver = webdriver.Chrome()

# 前往登入頁面
driver.get("https://taichi.wuwow.tw/login")

# 找到並填寫帳號和密碼
username = driver.find_element(By.CSS_SELECTOR,'input[name=\"email\"]')
password = driver.find_element(By.CSS_SELECTOR,'input[name=\"password\"]')
username.send_keys("0900224882")
password.send_keys("changeop890")

# 找到並點擊登入按鈕
login_button = driver.find_element(By.CSS_SELECTOR,"button[type='button']")
login_button.click()

# 等待一段時間，以確保登入完成
import time
time.sleep(5)

# 檢查是否成功登入
if driver.current_url == "https://taichi.wuwow.tw/dojo":
    print("成功登入，目前位於 https://taichi.wuwow.tw/dojo 頁面")
else:
    print("登入失敗")

# 關閉瀏覽器
driver.quit()