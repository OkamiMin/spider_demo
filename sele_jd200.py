import time
from selenium import webdriver
from lxml import etree
url = "https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&suggest=1.def.0.V03&wq=biji&psort=3&click=0"
wd = webdriver.Chrome()
wd.get(url)
for i in range(1,5):
    js = "var q = document.documentElement.scrollTop=10000"
    wd.execute_script(js)
    time.sleep(3)
    tree = etree.HTML(wd.page_source)
    prices = tree.xpath(r'//ul[@class="gl-warp clearfix"]//div[@class="p-price"]/strong/i/text()')
    names = tree.xpath(r"//div[@class='p-name p-name-type-2']/a/em/text()[1]")
    if i == 4:
        prices = prices[0:20]
        names = names[0:20]
        for p,n in zip(prices,names):
            print(n+':'+p)
    else:
        for p,n in zip(prices,names):
            print(n+':'+p)
    print(i,len(prices))
    wd.find_element_by_class_name("pn-next").click()
wd.quit()
