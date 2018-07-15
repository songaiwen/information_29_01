import requests, re


# class Guoke(object):
#     def __init__(self):
#         self.url = 'https://www.guokr.com/ask/highlight/?page=1'
#         self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
#
#         self.first_pattern = re.compile('<h2><a target="_blank" href="(.*?)">(.*?)</a></h2>')
#
#
#     #1.发送请求请求数据
#     def send_request(self):
#         response = requests.get(self.url, headers=self.headers)
#         data = response.content.decode()
#         return data
#
#     #3.解析需要的数据
#     def analysis_data(self, data):
#         result_list = self.first_pattern.findall(data)
#         return result_list
#
#
#     #2.保存到本地文件查看
#     def write_file(self, data):
#         with open('07guoke.txt', 'a', encoding="utf-8") as f:
#             for result in data:
#                 f.write(result[1] + '\n')
#
#     #4.调度方法
#     def run(self):
#         data = self.send_request()
#         result_list = self.analysis_data(data)
#         self.write_file(result_list)
#
# if __name__ == '__main__':
#     Guoke().run()



class GuokeSpider(object):

    #1.初始化方法
    def __init__(self):
        self.url = 'https://www.guokr.com/ask/highlight/?page=1'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    #正则匹配我们需要拿到的内容链接
    #<a target="_blank" href="https://www.guokr.com/question/669761/">印度人把男人的生殖器叫林伽，把女人的生殖器叫瑜尼，林伽和瑜尼的交合，便是瑜伽。这是真还是假的</a>
    # 分析思路:_blank是不变的,所有的标题都会新开页面跳转到详情页
        #但是href内容不是固定不变的,每一个新闻对应一个编码,那我们都要拿到
        #标题内容也会变,所以也需要获取
        #<a target="_blank" href="(.*)">(.*)</a> 这种方式获取的数据并不精准,会匹配到所有带有a标签的标题内容,
        #那么遇到这样的情况我们可以往上面一层去查找,发现在外面加一层h2标签,而其他带a标签的外面没有h2标签,这样就可以使标题内容进一步精准
        #<h2><a target="_blank" href="(.*)">(.*)</a></h2>
        #注意问题:python字符串中  :单包双,双包单的角度书写是没有问题
        #但是正则中需要保留元是字符串 ,所以符号不能变
        self.pattern = re.compile('<h2><a target="_blank" href="(.*)">(.*)</a></h2>')
    #2.发送请求请求数据
    def send_request(self):
        data =requests.get(self.url, headers=self.headers).content.decode()

        return data
    #3.解析数据
    def analysis_data(self, data):
        result_list = self.pattern.findall(data)
        return result_list


    #4.保存数据
    def save_data(self, data):
        with open("06guoke.html", 'w') as f:
            f.write(data)
            print("保存成功")

    #5.调度方法
    def run(self):
        data = self.send_request()
        result_list = self.analysis_data(data)
        print(result_list)
        # self.save_data(result_list)


if __name__ == '__main__':
    GuokeSpider().run()





























