import time
from selenium import webdriver
from lxml import etree
import csv

def saveHtml(prices,names):
    header = ['name', 'price']
    with open('jd_demo.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, header)
        writer.writerow(dict(zip(header, header)))
        for p, n in zip(prices, names):
            print(n + ':' + p)
            writer.writerow({"name": n, "price": p})

def nextHtml(i):
    va = wd.find_element_by_xpath('//div[@class="p-wrap"]//input[@class="input-txt"]')
    va.clear()
    va.send_keys(i + 1)
    wd.find_element_by_xpath('//div[@class="p-wrap"]//a[@class="btn btn-default"]').click()
def main(num):
    for i in range(1,num+1):
        print(i)
        js = "var q = document.documentElement.scrollTop=10000"
        wd.execute_script(js)
        time.sleep(3)
        tree = etree.HTML(wd.page_source)
        prices = tree.xpath(r'//ul[@class="gl-warp clearfix"]//div[@class="p-price"]/strong/i/text()')
        names = tree.xpath(r"//div[@class='p-name p-name-type-2']/a/em/text()[1]")
        saveHtml(prices,names)
        nextHtml(i)
if __name__ == '__main__':
    num = int(input("请输入要抓取的页数:"))
    url = "https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&suggest=1.def.0.V03&wq=biji&psort=3&click=0"
    wd = webdriver.Chrome()
    wd.get(url)
    main(num)
    wd.quit()


