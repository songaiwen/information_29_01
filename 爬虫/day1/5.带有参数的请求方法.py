import requests

#方法一:url和参数拼接
"""
class Search_Spider(object):
    #初始化方法
    def __init__(self):
        self.search_word = input("请输入要查询的内容:")
        self.base_url = 'https://www.baidu.com/s?wd='
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    #发送请求
    def send_request(self,url):
        response = requests.get(url, headers=self.headers)
        data = response.content.decode()
        return data
    #保存数据
    def save_data(self,data):
        with open("05seacher2.html", 'w') as f:
            f.write(data)
    #调度方法
    def run(self):
        url = self.base_url + self.search_word
        data = self.send_request(url)
        self.save_data(data)

if __name__ == '__main__':
    tool = Search_Spider()
    tool.run()
"""

#方法二:利用params参数发送带参数的请求

class Search_Spider(object):
    #初始化方法
    def __init__(self):
        self.search_word = input("请输入要查询的内容:")
        self.base_url = 'https://www.so.com/s?q='
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    #发送请求
    def send_request(self, url, send_parms):
        response = requests.get(url, headers=self.headers, params=send_parms)
        data = response.content.decode()
        return data

    #保存文件
    def save_data(self, data):
        with open("05search3.html", 'w') as f:
            f.write(data)

    #调度方法
    def run(self):
        #拼接参数
        params = {
            'q':self.search_word
        }

        #发送请求
        data = self.send_request(self.base_url, send_parms=params)
        self.save_data(data)
if __name__ == '__main__':
    tool = Search_Spider()
    tool.run()






















