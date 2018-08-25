import requests

def load_data():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    }

    response = requests.get("http://www.baidu.com", headers = headers)
    data = response.content.decode()

    #请求cookie
    request_cookie = response.request._cookies

    #利用requests.utils.dict_from_cookiejar转成字典
    cook_dict = requests.utils.dict_from_cookiejar(request_cookie)

    print(cook_dict)

if __name__ == '__main__':
    load_data()
