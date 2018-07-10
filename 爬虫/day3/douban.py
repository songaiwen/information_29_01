import requests

class Douban_Spider(object):
    #初始化方法
    def __init__(self):
        self.base_url = "https://movie.douban.com/subject/26752088/?from=showing"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    #发送请求
    def send_request(self):
        proxy = {
            'http': '180.118.94.212:9000'
        }
        data = requests.get(self.base_url, headers=self.headers, proxies=proxy).content.decode()
        return data

    #保存数据
    def save_data(self, data):
        with open('01douban.html', 'w') as f:
            f.write(data)

    #调度方法
    def run(self):
        data = self.send_request()
        self.save_data(data)

if __name__ == '__main__':
    tool = Douban_Spider()
    tool.run()