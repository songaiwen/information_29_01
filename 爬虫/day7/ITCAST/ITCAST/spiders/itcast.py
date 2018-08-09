# -*- coding: utf-8 -*-
import scrapy

#继承basic模板,Spider
class ItcastSpider(scrapy.Spider):
    #爬虫名字
    name = 'itcast'
    #允许爬取的域名范围,确认爬取的内容
    allowed_domains = ['itcast.cn']
    #起始的url
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    #解析数据的方法,指定方法,必须这么写
    def parse(self, response):
        print("*" * 100)
        print(response.url)
