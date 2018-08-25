# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import requests
from bs4 import BeautifulSoup
import json


class TencentSpider(object):
    def __init__(self):
        self.base_url = 'https://hr.tencent.com/position.php'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        # 数据集合 list
        self.data_list = []

    # 1.发请求
    def send_request(self, tencent_params):
        try:
            data = requests.get(self.base_url, headers=self.headers, params=tencent_params).content.decode()
            return data
        except Exception as e:
            print(e)

    # 2.解析数据 xpath
    def analysis_data(self, data):
        # 1.转换成 解析类型
        html_data = BeautifulSoup(data, 'lxml')

        # 2. 解析数据 获取所有 tr 的标签对象 list
        tr_list = html_data.select('.even,.odd')

        # 3. 遍历每一个 tr; 取出 td 里面的内容 text()
        for tr in tr_list:
            dict_data = {}
            dict_data['work_position'] = tr.select('td a')[0].get_text()
            dict_data['work_type'] = tr.select('td')[1].get_text()
            dict_data['work_count'] = tr.select('td')[2].get_text()
            dict_data['work_place'] = tr.select('td')[3].get_text()
            dict_data['work_time'] = tr.select('td')[4].get_text()

            # 添加到 集合list
            self.data_list.append(dict_data)

    # 3.保存数据
    def write_file(self):

        json.dump(self.data_list, open('05tencent.json', 'w'))
        print('保存成功!')

    # 4.调度 run
    def run(self):

        # 1.拼参数
        tencen_prams = {
            "keywords": "python",
            "lid": "2156",
            "tid": "0",
            "start": "0"
        }
        # 2.发送请求
        data = self.send_request(tencent_params=tencen_prams)

        # 3.解析数据
        self.analysis_data(data)

        # 4.保存
        self.write_file()


if __name__ == '__main__':
    TencentSpider().run()
