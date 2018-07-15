# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import requests
from lxml import etree

import time

import threading
from queue import Queue


# 反爬 限制频率

class QiushiSpider(object):
    def __init__(self):
        self.base_url = 'https://www.qiushibaike.com/8hr/page/{}'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

        # 记录个数
        self.count = 0

        # 1. url队列
        self.url_queue = Queue()

        # 2. 响应对列
        self.response_queue = Queue()

        # 3. 数据队列
        self.data_queue = Queue()

    # 1.组合列表 url
    def get_url_list(self):
        # return [self.base_url.format(i) for i in range(1, 14)]
        # 入对垒 url
        for i in range(1, 14):
            self.url_queue.put(self.base_url.format(i))

    # 2. 发请求
    def send_request(self):
        while True:
            # 取出 url 对=列 中url
            url = self.url_queue.get()

            time.sleep(1)
            response = requests.get(url, headers=self.headers)
            print(response.url)

            if response.status_code == 200:

                # data = response.content.decode()

                # 入 response 队列
                self.response_queue.put(response)
            else:
                self.url_queue.put(url)

            # 计数器减一
            self.url_queue.task_done()

    # 3. 解析数据
    def analysis_data(self):
        while True:
            # 取出 response队列 中的数据
            data = self.response_queue.get().content.decode()

            # 1.转换类型
            html_data = etree.HTML(data)

            # 2.解析 所有的 段子
            div_list = html_data.xpath('//div[@id="content-left"]/div')

            print("解析个数:", len(div_list))
            for div in div_list:
                nick_name = div.xpath('.//h2/text()')[0]

                #  入数据 队列
                self.data_queue.put(nick_name)

            # 计数器减一
            self.response_queue.task_done()

    # 4.保存数据
    def save_data(self):
        while True:
            # 从 数据队列 取数据
            data = self.data_queue.get()

            print(data.strip())
            self.count += 1

            # 减一
            self.data_queue.task_done()

    # 调度任务
    def start_work(self):

        t_list = []

        # 1. urllsit 线程
        t_url = threading.Thread(target=self.get_url_list)
        t_list.append(t_url)

        # 1. request 线程
        for i in range(3):
            t_request = threading.Thread(target=self.send_request)
            t_list.append(t_request)

        # 1. 解析数据
        t_nanalysis = threading.Thread(target=self.analysis_data)
        t_list.append(t_nanalysis)

        # 1. save
        t_save = threading.Thread(target=self.save_data)
        t_list.append(t_save)

        # 线程守护 开启线程
        for t in t_list:
            t.setDaemon = True
            t.start()

        # 主线程等待
        for q in [self.url_queue, self.response_queue, self.data_queue]:
            q.join()

    # 5.run
    def run(self):

        start_time = time.time()

        # 执行任务
        self.start_work()

        end_time = time.time()

        print("总耗时:", end_time - start_time)
        print("总个数:", self.count)


if __name__ == '__main__':
    QiushiSpider().run()
