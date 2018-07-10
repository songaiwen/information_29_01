"""
使用超时参数能够加快我们整体的请求速度，但是在正常的网页浏览过成功，如果发生速度很慢的情况，我们会做的选择是刷新页面

retrying的使用:
    使用retrying模块提供的retry模块
    通过装饰器的方式使用，让被装饰的函数反复执行
    retry中可以传入参数stop_max_attempt_number,让函数报错后继续重新执行，达到最大执行次数的上限，如果每次都报错，整个函数报错，如果中间有一个成功，程序继续往后执行

在请求中对于超时链接我们该怎么处理?
    请求方法中添加timeout能够实现强制程序返回结果的能够，否则会报错
    retrying模块能够实现捕获函数的异常，反复执行函数的效果，和timeout配合使用，能够解决网络波动带来的请求不成功的问题
"""

import requests
from retrying import retry

class Retry_Request(object):
    def __init__(self):
        self.url = "http://baidu"
        self.index = 0

    #使用装饰器的方式来限定我们最大的请求次数是5,5次都不满足条件,就根据断言弹出异常
    @retry(stop_max_attempt_number = 5)
    def _request_retry(self):
        self.index += 1
        print(self.index)
        #因为请求的url是错误的,肯定是不成功的,但是此时就只请求了一次
        response = requests.get(self.url)
        #断言
        assert response.status_code == 200
        return response.content.decode()

    def run(self):
        #调用上面的方法的时候,捕获异常并打印出来
        try:
            data = self._request_retry()
            print(data)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    Retry_Request().run()

