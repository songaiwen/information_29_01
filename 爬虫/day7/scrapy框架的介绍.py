"""
Scrapy框架的介绍
    Scrapy是用纯Python实现一个为了爬取网站数据、提取结构性数据而编写的应用框架，用途非常广泛。

    框架的力量，用户只需要定制开发几个模块就可以轻松的实现一个爬虫，用来抓取网页内容以及各种图片，非常之方便。

    Scrapy 使用了 Twisted['twɪstɪd](其主要对手是Tornado)异步网络框架来处理网络通讯，可以加快我们的下载速度，
    不用自己去实现异步框架，并且包含了各种中间件接口，可以灵活的完成各种需求。


"""

"""
Scrapy流程:
    Scrapy Engine:引擎组件,负责其他组件的交互通信和协调(总司令,发号施令)

    Scheduler(调度器):作为请求对象的中转站(缓存下载器暂时无法处理的请求对象,对请求进行去重)

    Downloader（下载器中间件）：(类似一个过滤器) 对请求对象和相应对象进行预处理

    Spider（爬虫）：构建请求信息(url,method,headers,paroms,data),解析响应,分析响应数据的数据结构或者页面结构
                    提取需要的数据, 提取新的请求地址

    Item Pipeline(管道)：对数据进行存储/对新的请求地址重复前面的步骤

    Downloader Middlewares（下载中间件）：发起HTTP/HTTPS请求,获取响应

    Spider Middlewares（Spider中间件）：对请求对象和数据对象进行预处理

爬虫的基本流程:
    1.构建请求信息(url, method, headers, porams, data)
    2.发起HTTP/HTTPS请求,获取HTTP/HTTPS响应
    3.解析响应,分析响应数据的数据结构或者页面结构提取需要的数据,提取新的请求地址
    4.对数据进行存储/对新的请求地址重复前面的步骤

"""
"""
制作Scrapy爬虫一共需要四步:
    新建项目 (scrapy startproject xxx)：新建一个新的爬虫项目
    明确目标 （编写items.py）：明确你想要抓取的目标
    制作爬虫 （spiders/xxspider.py）：制作爬虫开始爬取网页
    存储内容 （pipelines.py）：设计管道存储爬取内容

"""
#爬虫的命令可以使用scrapy来查看
#scrapy bench 命令是测试性能的.
#scrapy fetch "http://www.baidu.com/"  测试爬去百度页面
#scrapy shell "http://www.baidu.com/"  类似与在shell环境下操作,可以查看一些内容

"""
1.创建项目
    scrapy startproject Myspider
2.进入到项目目录mySpider/spider中,创建爬虫,名字为baidu,并指定爬取的域的范围
    scrapy genspider  baidu "http://www.baidu.com"
    目录中会默认添加一个baidu.py的文件,默认增加以下代码
    import scrapy

    class ItcastSpider(scrapy.Spider):
        #这个爬虫的识别名称，必须是唯一的，在不同的爬虫必须定义不同的名字。
        name = "baidu"
        #是搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页，不存在的URL会被忽略
        allowed_domains = ["http://www.baidu.com"]
        #爬取的URL元祖/列表。爬虫从这里开始抓取数据，所以，第一次下载的数据将会从这些urls开始。其他子URL将会从这些起始URL中继承性生成。
        start_urls = (
            'http://www.baidu.com',
        )

        #解析的方法，每个初始URL完成下载后将被调用，调用的时候传入从每一个URL传回的Response对象来作为唯一参数
        #1.负责解析返回的网页数据(response.body)，提取结构化数据(生成item)
        #2.生成需要下一页的URL请求。
        def parse(self, response):
            pass

"""

"""
scrapy默认可以输出四种常用文件方式
第一:json---------->scrapy crawl itcast -o itcast.json   json格式，默认为Unicode编码
第二:csv----------->scrapy crawl itcast -o itcast.csv    csv 逗号表达式，可用Excel打开
第三:jsonl--------->scrapy crawl itcast -o teachers.jsonl  json lines格式，默认为Unicode编码
第四:xml----------->scrapy crawl itcast -o teachers.xml    xml格式

"""





"""


"""




















