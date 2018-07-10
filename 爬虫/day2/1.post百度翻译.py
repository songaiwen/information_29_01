"""
百度翻译,是做了反爬的,所以我们用另外一种方式,通过移动端app也可以爬取
注意头要用移动端的请求头.
1.使用request发送post请求的使用场景:
    登录注册（ POST 比 GET 更安全）
    需要传输大文本内容的时候（ POST 请求对数据长度没有要求）
"""

import requests, json

def baidu_fanyi():
    translate_content = input("请输入要翻译的内容:")
    #在页面调试工具Network获取,通过XHR筛选得出
    #想要找到token内容可以用调试工具右面全局的search,然后用{}格式化一下.
    url = 'http://fanyi.baidu.com/basetrans'
    #带移动端的浏览器请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'
    }
    #传输的参数,data是字典形式
    data = {
        'query':translate_content,
        'from':'zh',
        'to':'en'

    }
    #发送请求
    response = requests.post(url, data=data, headers=headers)
    #得到数据解码保存
    result = response.content.decode()
    #将数据转换成
    dict_data = json.loads(result)

    result = dict_data['trans'][0]['result'][0][1]
    print("翻译的结果是:", result)

if __name__ == '__main__':
    baidu_fanyi()


