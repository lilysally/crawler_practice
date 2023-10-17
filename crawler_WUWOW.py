import requests
from bs4 import BeautifulSoup
session_requests = requests.session()
result = session_requests.get("https://taichi.wuwow.tw/login")
soup = BeautifulSoup(result.text, "html.parser")

_token_1 = soup.find_all("input")[0].get("value")
_token_2 = soup.find_all("input")[1].get("value")

login_data = {
    "_token": _token_1,
    "_token": _token_2,
    "account": "0900224882",
    "password": "changeop890",
}
headers = {
'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
"Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}

result = session_requests.post("https://taichi.wuwow.tw/login", data=login_data, headers=headers)
if result.history:
    print("Request was redirected")
    for resp in result.history:
        print(resp.status_code, resp.url)
    print("Final destination:")
    print(result.status_code, result.url)
else:
    print("Request was not redirected")