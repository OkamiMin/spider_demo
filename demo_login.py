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
reql = Request(login_url,headers=headers,data=f_data.encode())
c_handler = HTTPCookieProcessor(CookieJar())
opern = build_opener(c_handler)
respl = opern.open(reql)

req2 = Request(info_url,headers=headers)
resp2 = opern.open(req2)

print(resp2.read().decode())