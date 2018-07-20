# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    # 爬虫名字
    name = 'tencent'
    # 允许爬去的范围
    allowed_domains = ['tencent.com']

    start_urls = ['https://hr.tencent.com/position.php?keywords=python&tid=0&lid=2156&start=0']

    def parse(self, response):
        print(response.url)

        # 1. 取出 所有 tr_list
        tr_list = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')

        # 2.遍历 取出 td详细的数据
        for tr in tr_list:

            # 创构建item
            item = TencentItem()

            # 职位名称
            item['work_name'] = tr.xpath('./td[1]/a/text()').extract_first()
            # 职位类别
            item['work_type'] = tr.xpath('./td[2]/text()').extract_first()
            # 人数
            item['work_count'] = tr.xpath('./td[3]/text()').extract_first()
            # 地点
            item['work_place'] = tr.xpath('./td[4]/text()').extract_first()
            # 发布时间
            item['work_time'] = tr.xpath('./td[5]/text()').extract_first()
            # 详情页
            item['work_link'] = 'https://hr.tencent.com/' + tr.xpath('./td[1]/a/@href').extract_first()

            # 解析完毕的数据--引擎 -->管道pipeline
            yield item