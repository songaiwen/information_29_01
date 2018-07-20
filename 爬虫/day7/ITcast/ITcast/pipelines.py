# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

"""
当Item在Spider中被收集之后，它将会被传递到Item Pipeline，这些Item Pipeline组件按定义的顺序处理Item。

每个Item Pipeline都是实现了简单方法的Python类，比如决定此Item是丢弃而存储。以下是item pipeline的一些典型应用：

验证爬取的数据(检查item包含某些字段，比如说name字段)
查重(并丢弃)
将爬取结果保存到文件或者数据库中

"""

import json
#管道文件就是处理爬虫文件中返回的item数据的
#注意去setting文件里面打开管道,可以设置多个管道,管道里面的值越小,优先级越高
class ItcastPipeline(object):
    #可选的初始化文件
    def __init__(self):
        self.f = open("itcast_pipeline.json", "w")

    #默认生成这个方法,爬虫文件返回的item就返回到这个item里面
    def process_item(self, item, spider):
        #处理item字段,将item强转成dict,如果有中文使用ensure_ascii
        #表示处理中文的时候默认用unicode来存储
        content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.f.write(content.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.f.close()