# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import requests
from lxml import etree

import time

# 反爬 限制频率

class QiushiSpider(object):
    def __init__(self):
        self.base_url = 'https://www.qiushibaike.com/8hr/page/{}'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

        # 记录个数
        self.count = 0

    # 1.组合列表 url
    def get_url_list(self):
        return [self.base_url.format(i) for i in range(1, 14)]

    # 2. 发请求
    def send_request(self, url):
        time.sleep(1)
        response = requests.get(url, headers=self.headers)
        data = response.content.decode()
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

    # 调度任务
    def start_work(self):

        # 1.获取urllist
        url_list = self.get_url_list()

        # 2.执行循环
        for url in url_list:
            # 发送请求
            data = self.send_request(url)

            self.analysis_data(data)

            # 保存
            # self.save_data(data)

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
