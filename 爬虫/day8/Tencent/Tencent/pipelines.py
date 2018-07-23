# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

from .items import TencentItem, TencentDetailItem


# 列表管道
class TencentListPipeline(object):
    def open_spider(self, spider):
        self.file = open('list.json', 'w')

    def process_item(self, item, spider):
        if isinstance(item, TencentItem):
            json.dump(dict(item), self.file)
        return item

    def close_spider(self, spider):
        self.file.close()


# 详情页管道
class TencentDetailPipeline(object):
    def open_spider(self, spider):
        self.file = open('detail.json', 'w')

    def process_item(self, item, spider):
        if isinstance(item, TencentDetailItem):
            json.dump(dict(item), self.file)
        return item

    def close_spider(self, spider):
        self.file.close()
