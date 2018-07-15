import requests, re, json

class NeihanbaSpider(object):

    #1.初始化方法
    def __init__(self):
        #url
        self.base_url = 'https://www.neihan8.com/article/list_5_'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

        # 1.解析第一层 数据取出所有的数据
        #检查网页源代码<div class="f18 mb20"><p>老师:“小明，你的梦想是什么？”小明沉思片刻道:“有房有铺，自己当老板，妻子貌美如花，还有当官的兄弟” 老师:北宋有个人和你一样，他姓武！</p></div>
        #p标签里面的内容都需要拿到 所以得到<div class="f18 mb20">(.*?)</div>  因为由换行,需要匹配\n,所以需要加上re.S
        self.first_pattern = re.compile('<div class="f18 mb20">(.*?)</div>', re.S)

        #2.通过第一层解析,并没有完全取出纯文本数据,还需要去掉
            #1.标签    <(.*?)>
            #2.字符实体 &(.*?);
            #3.空白符   \s

        self.second_pattern = re.compile('<(.*?)>|&(.*?);|\s')

    #2.发送请求请求数据
    def send_request(self, url):
        #原网页是gbk字符集,linux和mac默认是utf-8,所以需要用gbk编码
        data = requests.get(url, headers=self.headers).content.decode('gbk')
        return data


    #3.解析需要的数据
    def analysis_data(self, data):
        result_list = self.first_pattern.findall(data)
        return result_list

    #4.保存到本地文件查看
    def write_file(self, data_list):
        with open('08neihanba2.txt', 'a') as f:
            for content in data_list:
                #过滤每一条端子中的多余内容
                new_content = self.second_pattern.sub('', content) + '\n'
                f.write(new_content)
            print('保存成功')

    #5.调度方法
    def run(self):
        #拼接url
        url = self.base_url + '1' + '.html'
        #1.发送请求数据
        data = self.send_request(url)

        #2.解析需要的数据
        # data_str = open('08neihanba.html', 'r', encoding='gbk').read()
        result_list = self.analysis_data(data)
        # print(result_list)

        # 3.保存到本地文件查看
        self.write_file(result_list)
        # with open("06neihanba2.html", 'a') as f:
        #     for result_str in result_list:
        #         f.write(result_str)

        # print(result_list)


if __name__ == '__main__':
    tool = NeihanbaSpider()
    tool.run()