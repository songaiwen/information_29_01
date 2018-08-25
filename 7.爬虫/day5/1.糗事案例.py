# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import requests


class QiushiSpider(object):
    def __init__(self):
        self.base_url = 'https://www.qiushibaike.com/8hr/page/{}'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 1.组合列表 url
    def get_url_list(self):
        return [self.base_url.format(i) for i in range(1, 2)]

    # 2. 发请求
    def send_request(self, url):
        response = requests.get(url, headers=self.headers)
        data = response.content.decode()
        return data

    # 3. 解析数据
    def analysis_data(self, data):
        pass

    # 4.保存数据
    def save_data(self, data):
        with open('01qiu.html', 'w') as f:
            f.write(data)

    # 5.run
    def run(self):
        # 1.获取urllist
        url_list = self.get_url_list()

        # 2.执行循环
        for url in url_list:
            # 发送请求
            data = self.send_request(url)
            # 保存
            self.save_data(data)



if __name__ == '__main__':
    QiushiSpider().run()
