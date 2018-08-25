"""
使用代理:
    让服务器以为不是同一个客户端在请求
    防止我们的真实地址被泄露，防止被追究

代理分类:
    透明代理(Transparent Proxy)：透明代理虽然可以直接“隐藏”你的IP地址，但是还是可以查到你是谁。
    匿名代理(Anonymous Proxy)：使用匿名代理，别人只能知道你用了代理，无法知道你是谁。

    高匿代理(Elite proxy或High Anonymity Proxy)：高匿代理让别人根本无法发现你是在用代理，所以是最好的选择。
我们使用的是高密

从请求使用的协议可以分为：
    http代理
    https代理
    socket代理等
    不同分类的代理，在使用的时候需要根据抓取网站的协议来选择

代理IP使用的注意点:
    反反爬
    使用代理ip是非常必要的一种反反爬的方式
    但是即使使用了代理ip，对方服务器任然会有很多的方式来检测我们是否是一个爬虫，比如：
    一段时间内，检测IP访问的频率，访问太多频繁会屏蔽
    检查Cookie，User-Agent，Referer等header参数，若没有则屏蔽
    服务方购买所有代理提供商，加入到反爬虫数据库里，若检测是代理则屏蔽
    所以更好的方式在使用代理ip的时候使用随机的方式进行选择使用，不要每次都用一个代理ip

代理ip池的更新:
    购买的代理ip很多时候大部分(超过60%)可能都没办法使用，这个时候就需要通过程序去检测哪些可用，把不能用的删除掉。

小结:
    在requests中使用代理，需要准备字典形式的代理，传递给proxies参数接收
    不同协议的url地址，需要使用不同的代理去请求

代理的使用:
     requests.get("http://www.baidu.com",  proxies = proxies),  proxies的形式：字典

"""


import requests

def proxy_base_use():
    url = 'http://www.baidu.com'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
    }

    proxy = {
        #使用免费的代理ip和端口号
        'http': '222.131.99.76:8118'

        # 付费代理
        # {'http':'username:pwd@IP:port'}
    }

    response = requests.get(url, headers=headers, proxies=proxy)
    print(response.status_code)

if __name__ == '__main__':
    proxy_base_use()




































