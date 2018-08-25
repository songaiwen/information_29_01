"""
response的常用属性：
    response.text            响应体 str类型
    respones.content         响应体 bytes类型
    response.status_code     响应状态码
    response.request.headers 响应对应的请求头
    response.headers         响应头
    response.request.cookies 响应对应请求的cookie
    response.cookies         响应的cookie（经过了set-cookie动作）

"""
import requests
def load_360_data():
    #1.获取url
    url = "https://www.so.com/"
    #2.发送请求
    response = requests.get(url)
    #3.输出数据---->str
    data = response.text
    #4.content---->bytes 优先使用content,在decode转成字符串
    data = response.content
    data = response.content.decode()
    #5.状态码
    code = response.status_code
    #6.请求头
    request_headers = response.request.headers
    #7.响应头
    response_headers = response.headers
    #8.cookie:请求
    request_cookie = response.request._cookies
    #9.cookie:响应
    response_cookie = response.cookies

    print(type(data))
    print(code)
    print(request_headers)
    print(response.headers)
    print(request_cookie)
    print(response_cookie)

if __name__ == '__main__':
    load_360_data()


#需求:下载一张图片,
def load_image():
    #目标url(360logo)
    url = "https://p.ssl.qhimg.com/t01d1f1a2ae31e3c3e4.png"
    #向目标url发送请求
    response = requests.get(url)
    # 获取数据
    image_data = response.content
    #以二进制的方式打开文件,并将response响应的二进制内容写入
    with open("03360.png", 'wb') as f:
        #写入response.content bytes二进制类型
        f.write(image_data)
        print("图片保存成功")

if __name__ == '__main__':
    load_image()

