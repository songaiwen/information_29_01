from selenium import webdriver
import time
from bs4 import BeautifulSoup


class DouyuSpider(object):
    def __init__(self):
        self.url = 'https://www.douyu.com/directory/all'
        self.driver = webdriver.Chrome()
        self.count = 0

    # 解析方法
    def analysis_data(self, data):
        # 1.转换类型
        soup = BeautifulSoup(data, 'lxml')

        # 2.解析 房间名字  主播昵称 热度
        room_list = soup.select('#live-list-contentbox .ellipsis')
        nick_list = soup.select('#live-list-contentbox .dy-name')
        hot_list = soup.select('#live-list-contentbox .dy-num')

        for room, nick, hot in zip(room_list, nick_list, hot_list):
            print(room.get_text().strip() + "==", nick.get_text().strip() + "==", hot.get_text().strip())
            self.count += 1

    # 调度
    def run(self):
        self.driver.get(self.url)
        time.sleep(3)
        data = self.driver.page_source
        self.analysis_data(data)

        print("总个数:", self.count)

        self.driver.quit()

if __name__ == '__main__':
    DouyuSpider().run()