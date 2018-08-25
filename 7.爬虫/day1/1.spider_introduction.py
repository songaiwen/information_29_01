#第一部分:爬虫的介绍和简单案例
"""
1.什么是爬虫?
抓取网页数据的程序

2.爬虫如何抓取网页数据的
    2.1网页的三大特征
        每个网页都有自己的url(统一资源定位符)来定位网页的位置,每一个网页都有唯一的一个url,每一个url都有对应的网页
        网页都使用HTMl(超文本标记语言)来描述网页的页面信息
        网页都使用HTTP或者是HTTPS(超文本传输协议)来传输HTMl数据
    2.2爬虫设计思路
        首先找到需要爬去的网页url地址
        通过http协议来获取对应HTML页面
        提取HTMl页面里面的数据
            如果是需要保存的数据,保存起来
            如果需要继续抓取的url,继续抓取这个url
    2.3爬虫原理:
        目标url
        发送请求获取数据
        解析,清洗,分析数据
        入库-一般是非关系型数据库

3.为什么选择python做爬虫?
    1. Java：Java的网络爬虫生态圈也很完善，是Python爬虫的头号对手。
        但是Java语言比较笨重，代码量非常大，后期维护修改会导致代码大量变动，开发成本和重构成本比较高。
    2. PHP：虽然是世界上最好的语言，但是它天生不是干爬虫的。对多线程、异步支持比较差，并发处理能力弱，爬虫本身是工具型程序，对速度和效率要求非常高。
    3. C/C++：运行效率和性能几乎最强，但是学习成本比较高。导致开发成本高。用C/C++写爬虫，是能力的表现，但不是最好的选择。
    4. Python：语法优美简洁，代码编写快速方便，开发效率高，工具集齐全，学习成本低。
    在爬虫方面，相关的HTTP请求类库和HTML解析类库非常丰富，调用其他接口也很方便。而且有强大的爬虫框架Scrapy、以及高效成熟的分布式策略 scrapy-reids

4.内容介绍
    1.Python基础语法学习（基础知识）
    2. HTML页面的抓取：
        urllib、urllib2、requests，通过处理HTTP请求，可以模拟浏览器发送HTTP请求，获取服务器响应的HTML页面。
    3. HTML页面内容的提取：
        re、xpath(lxml)、BeautifulSoup、jsonpath，通过解析HTML页面，通过某种描述性的语言来提取页面数据。凡是符合这个规则的数据，我们就叫"匹配"。
    4. 动态html页面处理、验证码处理
        Selenium + PhantomJS，模拟真实浏览器加载HTML、JS、AJAX等动态页面数据。
        Tesseract OCR:光学字符识别系统：可以用来识别图片上的文字。
    5. Scrapy框架 scrapy-redis分布式策略：
        scrapy:高定制性、高性能的Python爬虫框架，提供了数据存储、数据下载、提取规则、请求并发处理、请求去重等等组件。同时使用了twisted异步网络框架。
        scrapy-redis：分布式策略：在Scrapy框架的基础上提供了一套以Redis为核心的组件，让Scrapy拥有支持分布式的功能。
        主要是在同一个Redis数据库里做：请求的分配、请求的去重、数据的存储。
    -6 7.爬虫 -  反爬虫 = 反反爬虫 ... 之间的斗争
    其实爬虫做到最后你会发现，最让我们头疼的不是爬虫的语法，也不是复杂的页面，而是网站另一边的反爬虫工程师。
    User-Agent、代理IP、Cookies、验证码、动态数据加载、加密数据。

5.爬虫的类型:通用爬虫和聚焦爬虫
    通用爬虫:指搜索引擎和大型web服务提供商的爬虫
    聚焦爬虫:针对特定的网站爬虫,定向的获取某方面数据的爬虫
        累积式爬虫:从开始到结束,不断爬取,过程中会进行去重操作
        增量式爬虫:已下载网页采取增量式更新和只爬行新产生的或者已经发生变化的网页爬虫
        Deep web爬虫:不能通过静态链接获取的,隐藏在搜索表单后的,只有用户提交一些关键词才能获得的web页面

6.HTTP和HTTPS
    HTTP(超文本标记语言,默认端口号:80)
    HTTPS(超文本传输协议,默认端口号:443)  ,HTTPS比HTTP更安全，但是性能更低
    浏览器发送HTTP请求的过程:
        1.浏览器先向地址栏中的url发起请求，并获取响应
        2.在返回的响应内容（html）中，会带有css、js、图片等url地址，以及ajax代码，浏览器按照响应内容中的顺序依次发送其他的请求，并获取相应的响应
        3.浏览器每获取一个响应就对展示出的结果进行添加（加载），js，css等内容会修改页面的内容，js也可以重新发送请求，获取响应
        4.从获取第一个响应并在浏览器中展示，直到最终获取全部响应，并在展示的结果中添加内容或修改————这个过程叫做浏览器的渲染
    HTTP常见请求头:
        Host (主机和端口号)
        Connection (链接类型)
        Upgrade-Insecure-Requests (升级为HTTPS请求)
        User-Agent (浏览器名称)
        Accept (传输文件类型)
        Referer (页面跳转处)
        Accept-Encoding（文件编解码格式）
        Cookie （Cookie）
        x-requested-with :XMLHttpRequest (表示该请求是Ajax异步请求)
    HTTP重要的响应头:
        Set-Cookie （对方服务器设置cookie到用户浏览器的缓存）
    常见响应状态码:
        200：成功
        302：临时转移至新的url
        307：临时转移至新的url
        404：找不到该页面
        500：服务器内部错误
        503：服务不可用，一般是被反爬
    注意点:
    但是在爬虫中，爬虫只会请求url地址，对应的拿到url地址对应的响应（该响应的内容可以是html，css，js，图片等）
    浏览器渲染出来的页面和爬虫请求的页面很多时候并不一样

7.字符,字符集
    字符(Character):是各种文字和符号的总称，包括各国家文字、标点符号、图形符号、数字等
    字符集(Character set):是多个字符的集合
    字符集包括：ASCII字符集、GB2312字符集、GB18030字符集、Unicode字符集等
    ASCII编码是1个字节，而Unicode编码通常是2个字节。
    UTF-8是Unicode的实现方式之一，UTF-8是它是一种变长的编码方式，可以是1，2，3个字节

    str 使用encode方法转化为 bytes
        s = 'abc'
        print(type(s))   <class 'str'>
        #str编码变为bytes类型
        b = s.encode
        print(type(b))   <class 'builtin_function_or_method'>

    bytes 通过decode转化为 str
        b = b'abc'
        print(type(b))
        #bytes类型解码成为str类型
        s = b.decode()
        print(type(s))

8.为什么重点学习request?
    requests的底层实现就是urllib
    requests在python2 和python3中通用，方法完全一样
    requests简单易用
    Requests能够自动帮助我们解压(gzip压缩的等)响应内容

9.爬虫的用途:
    进行在网页或者app上展示
    进行数据分析或者是及其学习相关的项目

10.robots协议:
    robots.txt是搜索引擎中访问网站的时候要查看的第一个文件。当一个搜索蜘蛛访问一个站点时，
    它会首先检查该站点根目录下是否存在robots.txt，如果存在，搜索机器人就会按照该文件中的内容来确定访问的范围；
    如果该文件不存在，所有的搜索蜘蛛将能够访问网站上所有没有被口令保护的页面。
"""

import requests

def load_baidu():
    #获取url目标
    url = "http://www.baidu.com/"
    #向目标url发送请求
    response = requests.get(url)
    #接受响应数据,并打印
    data = response.text
    print(type(data))

if __name__ == '__main__':
    load_baidu()




















