# !/usr/bin/env python
# _*_ coding:utf-8 _*_

import scrapy
from ITCAST.items import ItcastItem
class ITcastSpider(scrapy.Spider):
    name = "itcast2"

    allowed_domains = ['itcast.cn']

    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        #1.取出所有符合条件div_list
        div_list = response.xpath("/html/body/div[1]/div[5]/div[2]/div[2]/ul/li/div")

        #2.遍历div解析出详细的数据
        for div in div_list:
            #xpath取出来的值是列表,取里面的第一个元素,然后再用extract转一下,成为我们想要的数据
            print(div.xpath("./h3/text()")[0].extract())
            #item里面的key如果写错,会报错
            dict_data = ItcastItem()
            dict_data['name'] = div.xpath("./h3/text()")[0].extract()
            dict_data['position'] = div.xpath("./h4/text()")[0].extract()
            dict_data['info'] = div.xpath("./p/text()")[0].extract()

            print(dict_data)
            #解析出来的数据给了引擎,然后给管道pipeline
            yield dict_data
