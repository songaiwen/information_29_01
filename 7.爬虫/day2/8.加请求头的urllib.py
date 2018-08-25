import urllib.request

def load_data():
    url = "http://www.baidu.com"
    #构造headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"
    }
    #构造请求urllib.request.Request(url,headers,data)能够构造请求
    request = urllib.request.Request(url, headers=headers)
    #使用add_header添加
    request.add_header('Connection', '123')
    #urllib.request.urlopen能够接受request请求或者url地址发送请求，获取响应
    response = urllib.request.urlopen(request)
    #对应的使用get_header取相应的数据
    request_user_agent = request.get_header('Connection')
    print(request_user_agent)

    #response.read()能够实现获取响应中的bytes字符串
    data = response.read()
    print(data)


if __name__ == '__main__':
    load_data()

#注意点:获取请求头信息时key首字母大写,其他的都是小写
def load_baidu():
    url = "http://www.baidu.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"
    }
    #请求对象
    request = urllib.request.Request(url, headers=headers)
    #发送请求request对象
    response = urllib.request.urlopen(request)

    #获取请求头的信息-key首字母大写,其他的都是小写
    request_user_agent = request.get_header("User-agent")
    print(request_user_agent)

if __name__ == '__main__':
    load_baidu()


