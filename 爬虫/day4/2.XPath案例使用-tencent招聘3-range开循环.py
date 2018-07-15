import requests
from lxml import etree
import json

class TencentSpider(object):
    #初始化方法
    def __init__(self):
        self.base_url = 'https://hr.tencent.com/position.php?'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        #先等数据全部加载完了,一起在保存到数据库
        self.data_list = []
    #2.发送请求
    def send_request(self, tencent_params):
        try:
            response = requests.get(self.base_url, headers=self.headers, params=tencent_params)
            data =response.content.decode()
            print(response.url)
            return data
        except Exception as e:
            print(e)

    #3.解析数据
    def analysis(self, data):
        #1.转换成解析的类型
        html_data = etree.HTML(data)
        #2.解析数据,获取所有的tr的标签对象  类型是list
        tr_list = html_data.xpath('//tr[@class="even"] | //tr[@class="odd"]')
        # print(len(tr_list))
        #3.遍历每一个tr,取出td里面的内容text()
        for tr in tr_list:
            dict_data = {}
            dict_data['work_position'] = tr.xpath('td/a/text()')[0]
            dict_data['work_type'] = tr.xpath('td[2]/text()')[0]
            dict_data['work_count'] = tr.xpath('td[3]/text()')[0]
            dict_data['work_place'] = tr.xpath('td[4]/text()')[0]
            dict_data['work_time'] = tr.xpath('td[5]/text()')[0]

            #添加数据到列表list中
            self.data_list.append(dict_data)
    #4.保存数据
    def write_file(self):
        json.dump(self.data_list, open('02tencent.json', 'w'))
        print("保存成功")

    def run(self):
        #的后动写固定的循环范围,每页10条数据
        for page in range(0,90,10):
            #1.拼接参数
            tencent_params = {
                "keywords": "python",
                "lid": "2175",
                "tid": "0",
                "start": "page",
            }
            #2.发送请求
            data = self.send_request(tencent_params=tencent_params)

            #3.解析数据
            self.analysis(data)
        #4.保存
        self.write_file()

if __name__ == '__main__':
    TencentSpider().run()