# -*- coding: utf-8 -*-
import scrapy

#链接解析库
from scrapy.linkextractors import LinkExtractor
#爬虫类
from scrapy.spiders import CrawlSpider, Rule

#继承关系变了,继承自CrawlSpider
class TencentSpider(CrawlSpider):
    #爬虫名字
    name = 'tencent'
    #域名范围
    allowed_domains = ['tencent.com']
    #初始url
    start_urls = ['https://hr.tencent.com/position.php?keywords=&lid=0&tid=0']
    count = 0

    #CrawlSpider 对url会自动去重,直接异步并发
    #新增了rules元组
    #1.自动提取目标link url
    #2.自动发送request对象;经过下载器返回的response对象,继续解析,如果有目标url,继续发送请求
    rules = (
        #参数1:提取规则
        #参数2:回调解析函数, 数据,传递的是字符串
        #参数3:是否跟进,假如一共53页,如果跟进True是会全部爬取,如果不跟进False,就只能爬取首页能看到的页面,其余的不爬取

        #follow默认情况
        #callback 有 follow = False
        #callback 没有 follow = True

        #我们需要做的指定url规则,解析数据(data item)
        Rule(LinkExtractor(allow='start=\d+'), callback='abc_item', follow=True),
    )

    #解析方法,是自定义的
    def abc_item(self, response):

        print("*" * 50)
        print(response.url)
        self.count += 1
        print(("总的个数:", self.count))