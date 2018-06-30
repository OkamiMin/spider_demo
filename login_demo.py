# import requests
# login_url = "http://www.sxt.cn/index/login/login.html"
# info_url = "http://www.sxt.cn/index/user.html"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
# }
# form_data = {
#     "user": "17703181473",
#     "password": "123456"
# }
# session = requests.Session()
# session.post(login_url,headers=headers,data=form_data)
# # --------------------登陆-------------------------------
# requ1 = session.get(info_url,headers=headers)
# print(requ1.text)

from urllib.request import build_opener,Request,HTTPCookieProcessor
from http.cookiejar import CookieJar
from urllib.parse import urlencode

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}


login_url = "http://www.sxt.cn/index/login/login.html"
info_url = "http://www.sxt.cn/index/user.html"

form_data = {
    "user": "18895689552",
    "password": "liang2531wen"
}
f_data = urlencode(form_data)
req1 = Request(login_url,headers=headers,data=f_data.encode())
c_handler = HTTPCookieProcessor(CookieJar())#设置一个cookie处理器获取cookie
opern = build_opener(c_handler)#获得一个带有cookie的opern
resp1 = opern.open(req1)

req2 = Request(info_url,headers=headers)
resp2 = opern.open(req2)

print(resp2.read().decode())