# !/usr/bin/env python
# _*_ coding:utf-8 _*_


from selenium import webdriver
import time

def load_data():
    # 1.创建浏览器
    driver = webdriver.Chrome()

    # 2. 请求 首页
    driver.get('http://www.baidu.com')

    # 3. 点击新闻按钮
    driver.find_element_by_name('tj_trnews').click()

    # 4. 给输入框 输入内容
    driver.find_element_by_id('ww').send_keys('山争哥')

    # 5. 点击百度一下
    driver.find_element_by_class_name('btn').click()

    # 6.点击 第一条的新闻
    driver.find_element_by_xpath('//*[ @ id = "1"]/h3/a').click()


    # 由于 点击的标签 新开一个页面  回来的数据 还是老数据
    # 切换 window 页面
    print(driver.window_handles) #list
    driver.switch_to.window(driver.window_handles[1])


    time.sleep(2)
    # 保存快照
    driver.save_screenshot('02baidu.png')

    print('over....')


if __name__ == '__main__':
    load_data()



