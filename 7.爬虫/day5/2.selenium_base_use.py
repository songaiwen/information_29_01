

# !/usr/bin/env python
# _*_ coding:utf-8 _*_


from selenium import webdriver
import time

def load_data():
    # 1.创建浏览器
    # PhantomJS 过期了,目前使用的是selenium 2.48.2的版本就可以了
    # driver = webdriver.PhantomJS()
    driver = webdriver.Chrome()

    # 2.请求url
    driver.get('http://www.baidu.com')

    # 3.获取数据
    data = driver.page_source
    print(data)

    # 快照
    # driver.save_screenshot('o1baidu.png')

    # 标签
    news_el = driver.find_element_by_name('tj_trnews')

    # 标签包裹的内容
    print(news_el.text)

    # 取出属性
    print(news_el.get_attribute('href'))

    time.sleep(5)
    # 4. 关闭
    # 关闭页面
    driver.close()

    # 关闭浏览器
    driver.quit()

if __name__ == '__main__':
    load_data()

