# !/usr/bin/env python
# _*_ coding:utf-8 _*_


from selenium import webdriver
import time

def load_data():
    # 创建浏览器
    driver = webdriver.Chrome()

    # 2. 请求数据
    driver.get('http://www.itcast.cn/')

    # 执行js语句 操控页面 滚动到底
    js = 'window.scrollTo(0,document.body.scrollHeight)'

    driver.execute_script(js)

    time.sleep(5)
    driver.save_screenshot('03it.png')
    print('over')


if __name__ == '__main__':
    load_data()



