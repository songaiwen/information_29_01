# -*- coding: utf-8 -*-

import scrapy

from scrapy.linkextractors import LinkExtractor

from scrapy.spiders import CrawlSpider, Rule
from Tencent.items import TencentDetailItem, TencentItem


# 继承关系 CrawlSpider
class TencentSpider(CrawlSpider):
    name = "tencent2"
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?keywords=&lid=0&tid=0&start=0']

    # 新增了 rules 提取规则 自动提取
    # crawlspider 异步并发 所以 我们采用 2个item 2个管道 2个文件
    rules = (
        # 列表页 链接提取规则
        Rule(LinkExtractor(allow="start="), callback="parse_list", follow=True),
        # 详情页 链接提取规则
        Rule(LinkExtractor(allow="position_detail"), callback="parse_detail", follow=False)
    )

    # 解析数据
    def parse_list(self, response):
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


    def parse_detail(self, response):
        # 解析出 需要的ul list
        ul_list = response.xpath('//ul[@class="squareli"]')

        item = TencentDetailItem()
        # 职责
        item['work_duty'] = "".join(ul_list[0].xpath('./li/text()').extract())
        # 要求
        item['work_requir'] = "".join(ul_list[1].xpath('./li/text()').extract())

        # 解析完毕的详情页数据--引擎 -->管道pipeline
        yield item
