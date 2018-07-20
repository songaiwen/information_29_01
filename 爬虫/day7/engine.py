from .spider import Spider
from .pipeline import Spider
from .downloader import Spider
from .scheduler import Spider

class Engine(object):
    def __init__(self):
        self.spider = Spider()
        self.pipeline = Spider()
        self.downloader = Spider()
        self.scheduler = Spider()



    def start_work(self):

        #1.入口spider初始化url---引擎---调度入队列
        request = self.spider.start_request()
        self.scheduler.add_queue(request)
        #2.调度器出队列---引擎---下载器downloader(下载数据http.client)

        #3.下载器(response)---引擎--爬虫spider(解释数据url, item)

        #4.爬虫的解析结果---引擎---判断request(调度器) + item(pipeline)