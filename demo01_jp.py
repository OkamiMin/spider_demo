import requests
import jsonpath
import json
import re
#1.爬取
url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
           'referer':'https://www.lagou.com'}
response = requests.get(url,headers=headers)
info = response.text
#str
html = response.text
#2.解析
#str -->json object
obj = json.loads(html)
#2.2解析
#$..name
result = jsonpath.jsonpath(obj,'$..A..name')

print(result)
