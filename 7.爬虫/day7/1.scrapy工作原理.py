"""
1.scrapy框架介绍
    Scrapy是用纯Python实现一个为了爬取网站数据、提取结构性数据而编写的应用框架，用途非常广泛。

    框架的力量，用户只需要定制开发几个模块就可以轻松的实现一个爬虫，用来抓取网页内容以及各种图片，非常之方便。

    Scrapy 使用了 Twisted['twɪstɪd](其主要对手是Tornado)异步网络框架来处理网络通讯，可以加快我们的下载速度，不用自己去实现异步框架，并且包含了各种中间件接口，可以灵活的完成各种需求。


2.爬虫架构图中每个组件需要负责的内容
    调度器把requests-->引擎-->下载中间件--->下载器
    下载器发送请求，获取响应---->下载中间件---->引擎--->爬虫中间件--->爬虫
    爬虫提取url地址，组装成request对象---->爬虫中间件--->引擎--->调度器
    爬虫提取数据--->引擎--->管道
    管道进行数据的处理和保存

    Scrapy Engine(引擎): 负责Spider、ItemPipeline、Downloader、Scheduler中间的通讯，信号、数据传递等。

    Scheduler(调度器): 它负责接受引擎发送过来的Request请求，并按照一定的方式进行整理排列，入队，当引擎需要时，交还给引擎。

    Downloader（下载器）：负责下载Scrapy Engine(引擎)发送的所有Requests请求，并将其获取到的Responses交还给Scrapy Engine(引擎)，由引擎交给Spider来处理，

    Spider（爬虫）：它负责处理所有Responses,从中分析提取数据，获取Item字段需要的数据，并将需要跟进的URL提交给引擎，再次进入Scheduler(调度器)，

    Item Pipeline(管道)：它负责处理Spider中获取到的Item，并进行进行后期处理（详细分析、过滤、存储等）的地方.

    Downloader Middlewares（下载中间件）：你可以当作是一个可以自定义扩展下载功能的组件。

    Spider Middlewares（Spider中间件）：你可以理解为是一个可以自定扩展和操作引擎和Spider中间通信的功能组件（比如进入Spider的Responses;和从Spider出去的Requests）

3.三个内置对象
     请求对象(Request)
     响应对象(Response)
     数据对象(Item)

4.五个核心组件
     爬虫组件
         构建请求信息(初始的)，也就是生成请求对象(Request)
         解析响应对象，返回数据对象(Item)或者新的请求对象(Request)
     调度器组件
         缓存请求对象(Request)，并为下载器提供请求对象，实现请求的调度
         对请求对象进行去重判断
     下载器组件
         根据请求对象(Request)，发起HTTP、HTTPS网络请求，拿到HTTP、HTTPS响应，构建响应对象(Response)并返回
     管道组件
         负责处理数据对象(Item)
     引擎组件
         负责驱动各大组件，通过调用各自对外提供的API接口，实现它们之间的交互和协作
         提供整个框架的启动入口

5.两个中间件
     爬虫中间件
         对请求对象和数据对象进行预处理

     下载器中间件
         对请求对象和响应对象进行预处理


6.爬虫的流程
    1.构建请求信息(url、method、headers、params、data)
    2.发起HTTP/HTTPS请求，获取HTTP/HTTPS响应
    3.解析响应，分析响应数据的数据结构或者页面结构
        提取数据
        提取请求的地址
    4.对数据进行存储/对新的请求地址重复前面的步骤

"""