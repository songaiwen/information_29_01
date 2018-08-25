# -*- coding: utf-8 -*-
import scrapy
from ITcast.items import ItcastItem
"""
使用xpath取出姓名职称和介绍
//div[@class='li_txt']/h3
//div[@class='li_txt']/h4
//div[@class='li_txt']/p
"""

class ItcastSpider(scrapy.Spider):
    #爬虫名,启动爬虫时必须的参数
    name = 'itcast'
    #爬取域的范围,允许爬虫在这个域名下进行爬取(可选)
    allowed_domains = ['http://www.itcast.cn']
    #起始url列表,爬虫执行后第一批请求,将从这个列表里面获取
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    #固定不能变的名字和参数
    def parse(self, response):
        node_list = response.xpath("//div[@class='li_txt']")

        #存储所有item字段的,  在这里我们也可以用另外一种方法,即生成器
        # items = []

        for node in node_list:
            #创建item字段对象,用来存储信息
            item = ItcastItem()
            #可以直接使用xpath,返回的是xpath对象,通过extract转换成Unicode字符串
            name = node.xpath("./h3/text()").extract()
            title = node.xpath("./h4/text()").extract()
            info = node.xpath("./p/text()").extract()
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            # items.append(item)

            #获取数据交给pipelines,管道处理存储到数据库,这样就避免将所有的数据存储到一个数据类型
            #构成一个生成器,可以在下次调用的时候在本次停止的地方开始,并且在for循环里面可以一直循环,直到没有数据结束为止
            yield item
        # return items

