# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import requests
from lxml import etree


# 图片查找的过程: 1.贴吧列表页数 -->2.每个帖子详情 -->3.目标图片请求

class TiebaSpider(object):
    def __init__(self):
        self.tieba_name = '美食'
        self.base_url = 'https://tieba.baidu.com/f?kw=美食吧&pn=0'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

        # 1.第一层解析 详情的xpath list
        # self.first_xpath = '//a[@class="j_th_tit"]/@href'

        # self.first_xpath = '//a[@class="j_th_tit "]/@href' 正确的 有空格
        self.first_xpath = '//div[@class="t_con cleafix"]/div/div/div/a/@href'

        # 2.第二层解析 图片 xpath
        self.second_xpath = '//img[@class="BDE_Image"]/@src'

    # 1.发送请求
    def send_request(self, url):
        response = requests.get(url, headers=self.headers)
        data = response.content
        return data

    # 2.保存本地文件
    def save_data(self, data, image_name):
        file_name = 'images/' + image_name
        print(file_name)
        with open(file_name, 'wb') as f:
            f.write(data)


    def analysis_data(self, data, xpath_str):
        # 1.转换类型
        html_data = etree.HTML(data)

        # 2.解析
        result_list = html_data.xpath(xpath_str)

        return result_list

    # 3.调度
    def run(self):
        # 1.发送 列表 请求
        first_data = self.send_request(self.base_url)

        # 2. 发送详情页的请求
        # 2.1 详情url
        details_url_list = self.analysis_data(first_data, self.first_xpath)
        # 2.2 发送请求
        for link in details_url_list:
            url = 'http://tieba.baidu.com' + link
            details_data = self.send_request(url)

            # 3. 请求图片
            img_url_list = self.analysis_data(details_data, self.second_xpath)

            for img_url in img_url_list:
                image_data = self.send_request(img_url)

                # 保存图片
                image_name = img_url[-11:]
                self.save_data(image_data, image_name)

        print('保存完毕')



if __name__ == '__main__':
    tool = TiebaSpider()
    tool.run()
