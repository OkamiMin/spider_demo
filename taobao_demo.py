import time
from selenium import webdriver
from lxml import etree
import csv
url = "https://ai.taobao.com/search/index.htm?prepvid=200_10.176.85.19_89436_1530237349111&extra=&pid=mm_131341970_42712347_258128398&app_pvid=200_10.176.85.19_89404_1530237202869&channelId=5&cat=50000436&key=%E7%94%B7T%E6%81%A4&unid=&clk1=&source_id=&sort=&spm=a231o.7712113%2Ff.1003.d1"
wd = webdriver.Chrome()
wd.get(url)
for i in range(1,3):
    js = "var q = document.documentElement.scrollTop=10000"
    wd.execute_script(js)
    time.sleep(3)
    tree = etree.HTML(wd.page_source)
    prices = tree.xpath(r'//div[@class="search-result-box search-result-box2"]/div[@class="price clearfix"]/a[1]/em/text()')
    names = tree.xpath(r'//div[@class="search-result-box search-result-box2"]/div[@class="title"]/a[1]/text()[1]')
    sales = tree.xpath(r'//div[@class="search-result-box search-result-box2"]/div[@class="saleinfo"]/a/em/text()')
    header = ['name', 'price', 'sale']
    with open('taobao_demo.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, header)
        writer.writerow(dict(zip(header, header)))
        for p,n,s in zip(prices,names,sales):
            print(n+':'+p+':'+s)
    # print(i,len(prices))
            writer.writerow({"name": n, "price": p, "sale":s})
    wd.find_element_by_class_name("iconfont").click()
wd.quit()







