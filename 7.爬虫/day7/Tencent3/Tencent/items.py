# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # 职位名称
    work_name = scrapy.Field()
    # 职位类别
    work_type = scrapy.Field()
    # 人数
    work_count = scrapy.Field()
    # 地点
    work_place = scrapy.Field()
    # 发布时间
    work_time = scrapy.Field()
    work_link = scrapy.Field()

    # 职责
    work_duty = scrapy.Field()
    # 要求
    work_requir = scrapy.Field()


