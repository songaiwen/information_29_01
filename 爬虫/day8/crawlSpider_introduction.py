# !/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
CrawlSpider
创建爬虫 scrapy genspider -t crawl  爬虫名字xx  xx.com

LinkExtractor 链接提取器

1.自动提取目标url  link
2.自动发送request请求,解析response中子的目标url link


"""
"""
scrapy宽假提供了两个库
第一个:Spider
创建方式:genspider
倒包:import scrapy
继承关系:scrapy.Spider
属性:callback=self.xx
解析方法:指定的parse()

第二个:CrawlSpider
创建方式:genspider -t crawl
倒包:from scrapy.linkextractors import LinkExtractor
继承关系:CrawlSpider
属性:
解析方法:
"""