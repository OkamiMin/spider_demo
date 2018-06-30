from selenium import webdriver
from lxml import etree
import time

url = "https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90&action="
wd = webdriver.Chrome()
wd.get(url)

js = "var q = document.documentElement.scrollTop=10000"
wd.execute_script(js)

time.sleep(2)
e = etree.HTML(wd.page_source)
prices = e.xpath('//span[@class="movie-name-text"]/a/text()')
print(len(prices))
print(prices)

wd.quit()

