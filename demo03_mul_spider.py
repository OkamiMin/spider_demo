import queue
import threading
import requests
import time
from lxml import etree
'''
1.
url_queue
content_queue

2.线程
爬出线程：ThreadCrawl
解析线程：ThreadParser

3.爬取
crawl 领取url，url_queue
爬取结束，内容存入 content_queue

4.解析
parser，content_queue 领取任务
存入文件
'''


class ThreadCrawl(threading.Thread):
    def __init__(self,url_queue,content_queue):
        threading.Thread.__init__(self)
        self.url_queue = url_queue
        self.content_queue = content_queue

    def run(self):
        while True:
            if not self.url_queue.empty():
                url = self.url_queue.get()
                #爬取
                response = requests.get(url)
                self.content_queue.put(response.text)
            else:
                break



class ThreadParser(threading.Thread):
    def __init__(self,content_queue,file,lock):
        threading.Thread.__init__(self)
        self.content_queue = content_queue
        self.file = file
        self.lock = lock

    def run(self):
        while True:
            print('开始解析了。。。')
            # 解析：
            # // div[ @ id = "content-left"] / div / a / div / span
            if not self.content_queue.empty():
                content = self.content_queue.get()
                # 过程...
                e = etree.HTML(content)
                infos = e.xpath('// div[ @ id = "content-left"] / div / a / div / span/text()')
                #存储文件
                with self.lock:
                    #遍历列表
                    for info in infos :
                        a = info.strip()
                        self.file.write(a.encode())
                        self.file.flush()
                    print('解析结束。。。。')
            else:
                time.sleep(5)
                if  self.content_queue.empty():
                    break




if __name__ == '__main__':
    url_queue = queue.Queue()
    content_queue = queue.Queue()
    #url_queue  https://www.qiushibaike.com/text/page/2/
    for i in range(1,11):
        url = 'https://www.qiushibaike.com/text/page/{}/'.format(i)
        url_queue.put(url)
    print('开始解析了。。。')
    #爬取线程
    tc1 = ThreadCrawl(url_queue,content_queue)
    tc2 = ThreadCrawl(url_queue,content_queue)
    tc3 = ThreadCrawl(url_queue,content_queue)
    tc1.start()
    tc2.start()
    tc3.start()
    tc1.join()
    tc2.join()
    tc3.join()

    #解析线程
    file  = open('qiushibaike.txt','ab')
    lock = threading.Lock()
    tp1 = ThreadParser(content_queue,file,lock)
    tp2 = ThreadParser(content_queue,file,lock)
    tp3 = ThreadParser(content_queue,file,lock)

    tp1.start()
    tp2.start()
    tp3.start()
    tp1.join()
    tp2.join()
    tp3.join()
    print('全部完毕。。。。')
    file.close()
