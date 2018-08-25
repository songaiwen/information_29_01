# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import gevent.monkey
gevent.monkey.patch_all()
from gevent.pool import Pool

import requests
from lxml import etree

import time
from queue import Queue


# 反爬 限制频率

class QiushiSpider(object):
    def __init__(self):
        self.base_url = 'https://www.qiushibaike.com/8hr/page/{}'
        self.headers = {"User-Agent": "Mozilla/5.0 (Wind ows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"}

        # 记录个数
        self.count = 0

        # 创建 线程池
        self.pool = Pool(5)

        # url队列
        self.url_queue = Queue()

        # 请求个数
        self.request_num = 0
        # 响应的个数
        self.response_num = 0

        # 判断 是否递归
        self.running = True

    # 1.组合列表 url
    def get_url_list(self):
        # return [self.base_url.format(i) for i in range(1, 14)]
        for i in range(1, 14):
            self.url_queue.put(self.base_url.format(i))
            self.request_num  += 1

    # 2. 发请求
    def send_request(self, url):

        response = requests.get(url, headers=self.headers)
        data = response.content.decode()
        self.response_num += 1
        print(response.url)

        return data

    # 3. 解析数据
    def analysis_data(self, data):
        # 1.转换类型
        html_data = etree.HTML(data)

        # 2.解析 所有的 段子
        div_list = html_data.xpath('//div[@id="content-left"]/div')

        print("解析个数:", len(div_list))
        for div in div_list:
            nick_name = div.xpath('.//h2/text()')[0]
            print(nick_name.strip())
            self.count += 1

    # 4.保存数据
    def save_data(self, data):
        with open('01qiu.html', 'w') as f:
            f.write(data)

    # 任务

    # 调度任务
    def _excute_request_response_item(self):

        # 1.获取url从队列
        url = self.url_queue.get()
        # 2.发送请求
        data = self.send_request(url)
        # 3.解析数据
        self.analysis_data(data)

        # 减一
        self.url_queue.task_done()

    def _callback(self, item):
        if self.running:
            self.pool.apply_async(self._excute_request_response_item, callback=self._callback)

    # 5.run
    def run(self):

        start_time = time.time()
        # 1. 操作url
        self.get_url_list()

        # 异步调用任务 控制并发数:
        for i in range(3):
             self.pool.apply_async(self._excute_request_response_item, callback=self._callback)

        # 阻塞 主线程
        while True:
            # 避免循环空转 耗能
            time.sleep(0.00001)
            # 判断跳出  响应个数  大于等于 请求个数
            if self.response_num >= self.request_num:
                self.running = False
                break


        end_time = time.time()
        print("总耗时:", end_time - start_time)


if __name__ == '__main__':
    QiushiSpider().run()

