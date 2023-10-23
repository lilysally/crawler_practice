import requests
from bs4 import BeautifulSoup

# 建立一個 Session
session = requests.Session()

# 送出 GET 請求取得登入頁面，並取得 CSRF token
login_url = "https://taichi.wuwow.tw/login"
response = session.get(login_url)
soup = BeautifulSoup(response.text, "html.parser")
csrf_token = soup.select_one('input[name="_token"]')['value']

# 設定登入資訊
login_data = {
    "_token": csrf_token,
    "account": "0900224882",
    "password": "changeop890",
}

# 送出 POST 請求登入
response = session.post(login_url, data=login_data)

# 檢查是否成功登入
if response.url == "https://taichi.wuwow.tw/dojo":
    print("成功登入，目前位於 https://taichi.wuwow.tw/dojo 頁面")
else:
    print("登入失敗")

# 如果登入成功，你可以繼續使用 session 來訪問 https://taichi.wuwow.tw/dojo 頁面
