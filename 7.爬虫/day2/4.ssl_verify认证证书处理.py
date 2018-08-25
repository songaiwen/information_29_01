"""
requests处理证书错误

"""

import requests
def ssl_verify_data():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    }

    # 12306 证书 不是第三方认证; 浏览器会预警拦截
    #网址必须用的是加s的
    #出现这个问题的原因是：ssl的证书不安全导致,12306的认证是自己写的.
    url = 'https://www.12306.cn/mormhweb/'
    #如果没有我们就在发送请求的时候告诉系统,忽略证书
    response = requests.get(url, headers=headers, verify=False)
    print(response.content.decode())

if __name__ == '__main__':
    ssl_verify_data()
