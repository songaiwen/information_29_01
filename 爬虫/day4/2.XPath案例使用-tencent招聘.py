import requests
from lxml import etree
class TencentSpider(object):
    #初始化方法
    def __init__(self):
        self.base_url = 'https://hr.tencent.com/position.php?'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    #2.发送请求
    def send_request(self, tencent_params):
        data = requests.get(self.base_url, headers=self.headers, params=tencent_params).content.decode()
        return data

    #3.解析数据

    #4.保存数据
    def write_file(self, data):
        with open('02tencent.html', 'w') as f:
            f.write(data)
            print("保存成功")

    def run(self):
        #1.拼接参数
        tencent_params = {
            "keywords": "python",
            "lid": "2175",
            "tid": "0",
            "start": "0",
        }
        #2.发送请求
        data = self.send_request(tencent_params=tencent_params)

        #3.解析数据

        #4.保存
        self.write_file(data)

if __name__ == '__main__':
    TencentSpider().run()