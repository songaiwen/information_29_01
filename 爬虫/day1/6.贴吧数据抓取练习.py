# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import requests


class TiebaSpider(object):
    def __init__(self):
        self.tieba_name = input('请输入贴吧名字:')
        self.base_url = 'https://tieba.baidu.com/f?'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 1.发送请求
    def send_request(self, send_params):
        response = requests.get(self.base_url, headers=self.headers,params=send_params)
        data = response.content.decode()
        return data

    # 2.保存本地文件
    def save_data(self, data):
        with open('06tieba.html', 'w') as f:
            f.write(data)
            print('保存完毕')

    # 3.调度
    def run(self):
        # 拼接参数
        params = {
            'kw': self.tieba_name,
            'pn': 0
        }
        # 1.发送请求
        data = self.send_request(params)
        # 2.保存本地文件
        self.save_data(data)


if __name__ == '__main__':
    tool = TiebaSpider()
    tool.run()
