

# !/usr/bin/env python
# _*_ coding:utf-8 _*_


from selenium import webdriver
import time

def load_data():
    # 创建浏览器
    driver = webdriver.Chrome()

    # 2. 请求数据 http://127.0.0.1/frame.html
    driver.get('http://127.0.0.1/frame.html')

    # 3. 取 iframe 中 inpu贴标签
    #  driver.find_element 找不到

    # 切换到 iframe
    driver.switch_to.frame('loacFrame')

    # 再取标签
    input_el = driver.find_element_by_id('one')

    print(input_el.get_attribute('value'))

    # 从 iframe 框架返回
    # 1. 切换页面 switch_to.window(driver.window_handles[0])
    # 2. switch_to.default_content()

    driver.switch_to.default_content()
    up_el = driver.find_element_by_id('up')
    print(up_el.text)


    print('over')


if __name__ == '__main__':
    load_data()

