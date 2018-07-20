# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

from .items import TencentItem


class TencentPipeline(object):
    def open_spider(self, spider):
        self.file = open('tencentList.json', 'w')

    def process_item(self, item, spider):

        # 1.item - dict
        dict_data = dict(item)
        # 2.dict --str
        str_data = json.dumps(dict_data) + '\n'
        # 3.写入文件
        self.file.write(str_data)

        return item

    def close_spider(self, spider):
        self.file.close()
