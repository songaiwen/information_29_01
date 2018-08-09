"""
1.通过scrapy查看功能选项
      bench         Run quick benchmark test   测试demo
      check         Check spider contracts
      crawl         Run a spider
      edit          Edit spider
      fetch         Fetch a URL using the Scrapy downloader        查看url
      genspider     Generate new spider using pre-defined templates  创建爬虫
      list          List available spiders
      parse         Parse URL (using its spider) and print the results
      runspider     Run a self-contained spider (without creating a project)  运行爬虫,需要进到爬虫项目里面spiders找到爬虫名.py文件
      settings      Get settings values            设置文件
      shell         Interactive scraping console   测试终端
      startproject  Create new project             创建项目
      version       Print Scrapy version           查看版本
      view          Open URL in browser, as seen by Scrapy   打开浏览器

2.创建项目 scrapy startproject ITcast(项目名称)
  创建爬虫 scrapy genspider itcast(爬虫名字)  itcast.cn(允许爬取的域)
  运行爬虫1: scrapy crawl itcast(爬虫名字)
  运行爬虫2:进入到最里层的spiders文件里面找到 itcast.py文件  scrapy runspider itcast.py

3.解析数据:
    items.py  设置key字段
    itcast.py 解析数据response.xpath('').extract()[0]
                     response.xpath('')[0].extract()

    还有一个方法是使用extract_first 如果有值就是第一个,如果没有值返回None,不会报错.

4.存储数据:
    1.管道
    open_spider(self, spider)
    process_item(self, item, spider)
    close_spider(self, spider)

    2.scrapy crawl xx -o 文件名字json csv

    3.记得开启管道,在setting文件里面

5.setting:
    1.USER_AGENT = 'ITCAST (+http://www.yourdomain.com)'
    2.ROBOTSTXT_OBEY = True
    3.ITEM_PIPELINES = {
       'ITCAST.pipelines.ItcastPipeline': 300,
    }




"""





























































