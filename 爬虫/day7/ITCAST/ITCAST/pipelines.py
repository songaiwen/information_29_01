# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class ItcastPipeline(object):
    #1.爬虫打开的时机
    def open_spider(self, spider):
        self.file = open('itcast.json', 'w')

    #2.传递数据
    def process_item(self, item, spider):
        #1.将item转成dict
        dict_data = dict(item)
        #2.将dict转成str
        str_data = json.dumps(dict_data) + "\n"
        #3.写入
        self.file.write(str_data)
        return item

    #3.爬虫结束的时机
    def close_spider(self, spider):
        self.file.close()