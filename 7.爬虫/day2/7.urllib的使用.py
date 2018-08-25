"""
除了requests模块可以发送请求之外, urllib模块也可以实现请求的发送,只是操作方法略有不同!
python2使用的urllib2
python3使用的是urllib


"""
#倒包
import urllib.request

def load_baidu_data():
    #请求目标url
    url = "http://www.baidu.com"
    response = urllib.request.urlopen(url)
    #读取内容,返回的也是字节,需要decode处理
    data = response.read().decode()
    print(data)

if __name__ == '__main__':
    load_baidu_data()
