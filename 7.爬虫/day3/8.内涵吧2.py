# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import requests
import re


class NeihanBaSpider(object):
    def __init__(self):
        self.base_url = 'https://www.neihan8.com/article/list_5_'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

        # 1.第一层解析数据
        # <div class="f18 mb20">(.*)</div>
        self.first_pattern = re.compile('<div class="f18 mb20">(.*?)</div>', re.S)

        # 2.第二层解析
        # 1.标签          <(.*?)>
        # 2.字符实体       &(.*?);
        # 3,空白          \s

        self.second_pattern = re.compile('<(.*?)>|&(.*?);|\s')

    # 1.发请求
    def send_request(self, url):
        response = requests.get(url, headers=self.headers)
        # 原先网页 是gbk字符集 ; mac linux 默认utf-8; 所以 gbk
        data = response.content.decode('gbk')
        return data

    # 2.解析
    def analysis_data(self, data):
        result_list = self.first_pattern.findall(data)
        return result_list

    # 3.保存文件
    def write_file(self, data_list, page):
        # 拼接页数
        page_number = '----------------第' + str(page) + '页----------------\n\n'
        print(page_number)
        with open('08neihanba2.txt', 'a') as f:
            f.write(page_number)
            for content in data_list:
                # 过滤每一条段子中的多余内容
                new_content = self.second_pattern.sub('', content) + '\n'
                f.write(new_content)

            print('写入成功!')


    # 拼接大量uRL
    def get_url_list(self):
        url_list = []
        for page in range(1, 5):
            url = self.base_url + str(page) + '.html'
            url_list.append(url)
        return url_list

    # 4.run
    def run(self):

        # 根据urll列表循环
        url_list = self.get_url_list()

        for url in url_list:
            # 1.发送请求
            data = self.send_request(url)

            # 2. 解析数据
            result_list = self.analysis_data(data)

            # 3.保存数据
            page = url_list.index(url) + 1
            self.write_file(result_list, page)


if __name__ == '__main__':
    NeihanBaSpider().run()
