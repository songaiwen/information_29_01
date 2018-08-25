import requests

def get_baiduo():

    url = "https://www.baidu.com"
    #反爬的宗旨:模拟和用户一样的操作
    #带上user-agent
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    #发送请求
    response = requests.get(url,headers=headers)
    #获取请求头
    print(response.request.headers)
if __name__ == '__main__':
    get_baiduo()

