"""
1.什么是XML?
    XML 指可扩展标记语言（EXtensible Markup Language）
    XML 是一种标记语言，很类似 HTML
    XML 的设计宗旨是传输数据，而非显示数据
    XML 的标签需要我们自行定义。
    XML 被设计为具有自我描述性。
    XML 是 W3C 的推荐标准
2.什么是XPath?
    XPath (XML Path Language) 是一门在 XML 文档中查找信息的语言，可用来在 XML 文档中对元素和属性进行遍历。

3.XML的节点关系:
    1.父(Parent):每个元素以及属性都有一个父。
        demo:book 元素是 title、author、year 以及 price 元素的父
        <?xml version="1.0" encoding="utf-8"?>

        <bookstore>

        <book>
          <title>Harry Potter</title>
          <author>J K. Rowling</author>
          <year>2005</year>
          <price>29.99</price>
        </book>

        </bookstore>
    2.子(Children):元素节点可有零个、一个或多个子。
        上面的内容中:title、author、year 以及 price 元素都是 book 元素的子
    3.同胞（Sibling）:拥有相同的父的节点
        上面的内容中:title、author、year 以及 price 元素都是同胞
    4. 先辈（Ancestor）:某节点的父、父的父，等等。
        上面的内容中:title 元素的先辈是 book 元素和 bookstore 元素
    5. 后代（Descendant）:某个节点的子，子的子，等等。
        上面的内容中:bookstore 的后代是 book、title、author、year 以及 price 元素

4.XPath选取节点:
    1.表达式和描述信息
        表达式	            描述
        nodename	    选取此节点的所有子节点。
        /	            从根节点选取。
        //	            从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
        .	            选取当前节点。
        ..	            选取当前节点的父节点。
        @	            选取属性。



    demo:
    从上面的内容中,列出一些表达式的效果:
        bookstore	            选取 bookstore 元素的所有子节点。
        /bookstore	            选取根元素 bookstore。注释：假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！
        bookstore/book	        选取属于 bookstore 的子元素的所有 book 元素。
        //book	                选取所有 book 子元素，而不管它们在文档中的位置。
        bookstore//book	        选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。
        //@lang	                选取名为 lang 的所有属性。

    2.谓语的查找:用来查找某个特定的节点或者包含某个指定的值的节点,被嵌在方括号中.
        路径表达式	                                结果
        /bookstore/book[1]	                选取属于 bookstore 子元素的第一个 book 元素。  只有兄弟元素才可以使用下标,下标从1开始
        /bookstore/book[last()]	            选取属于 bookstore 子元素的最后一个 book 元素。
        /bookstore/book[last()-1]	        选取属于 bookstore 子元素的倒数第二个 book 元素。
        /bookstore/book[position()<3]	    选取最前面的两个属于 bookstore 元素的子元素的 book 元素。
        //title[@lang]	                    选取所有拥有名为 lang 的属性的 title 元素。
        //title[@lang=’eng’]	            选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。
        /bookstore/book[price>35.00]	    选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。
        /bookstore/book[price>35.00]/title	选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。

        注意点: 在xpath中，第一个元素的位置是1，最后一个元素的位置是last(),倒数第二个是last()-1

    3.未知节点的选取,使用通配符
        通配符	                  描述
        *	                匹配任何元素节点。
        @*	                匹配任何属性节点。
        node()	            匹配任何类型的节点。
    defmo:
        路径表达式	                        结果
        /bookstore/*	        选取 bookstore 元素的所有子元素。
        //*	                    选取文档中的所有元素。
        //title[@*]	            选取所有带有属性的 title 元素。

    4.选取若干路径:使用"|" 管道符号
        路径表达式	                                        结果
        //book/title | //book/price	            选取 book 元素的所有 title 和 price 元素。
        //title | //price	                    选取文档中的所有 title 和 price 元素。
        /bookstore/book/title | //price	        选取属于 bookstore 元素的 book 元素的所有 title 元素，以及文档中所有的 price 元素。

    5.XPath还有运算符,使用的时候查询即可

5.lxml库:lxml 是 一个HTML/XML的解析器，主要的功能是如何解析和提取 HTML/XML 数据。
        lxml和正则一样，也是用 C 实现的，是一款高性能的 Python HTML/XML 解析器，我们可以利用之前学习的XPath语法，来快速的定位特定元素以及节点信息。

"""

#demo:使用lxml的etree库
from lxml import etree

#demo1:
#lxml 可以自动修正 html 代码，例子里不仅补全了 li 标签，还添加了 body，html 标签。
if __name__ == '__main__':
    text = """
        <div>
            <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
             </ul>

    """
    #利用etree.HTML,将字符串解析为HTML文档
    html = etree.HTML(text)

    """
    注意点:
    可以发现，lxml确实能够把确实的标签补充完成，但是请注意lxml是人写的，很多时候由于网页不够规范，或者是lxml的bug，
    即使参考url地址对应的响应去提取数据，仍然获取不到，这个时候我们需要使用etree.tostring的方法，
    观察etree到底把html转化成了什么样子，即根据转化后的html字符串去进行数据的提取

    """
    # 按字符串序列化HTML文档
    result = etree.tostring(html).decode()
    print(result)
print("华丽的分割线=========================================================================================")

#demo2:
if __name__ == '__main__':
    # etree.parse() 方法来读取文件
    html = etree.parse('./hello.html')
    """
    外部文件实际内容
    <div>
        <ul>
             <li class="item-0"><a href="link1.html">first item</a></li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
    """
    # print(type(html))
    # result = etree.tostring(html, pretty_print=True).decode()
    # print(result)

    #1.获取所有的li标签
    """
    返回的是element对象，可以继续使用xpath方法，对此我们可以在后面的数据提取过程中：
    先根据某个标签进行分组，分组之后再进行数据的提取
    """
    result = html.xpath("//li")
    print(result)
    print(len(result))
    print(type(result))
    print(type(result[0]))
    print("华丽的分割线=========================================================================================")

    #2.继续获取<li> 标签的所有 class属性
    result = html.xpath('//li/@class')
    print(result)

    #3. 继续获取<li>标签下href 为 link1.html 的 <a> 标签
    result = html.xpath('//li/a[@href="link1.html"]')
    print(result)

    #4. 获取<li> 标签下的所有 <span> 标签
    result = html.xpath('//li//span')
    print(result)

    #5. 获取 <li> 标签下的<a>标签里的所有 class
    result = html.xpath('//li/a//@class')
    print(result)

    #6. 获取最后一个 <li> 的 <a> 的 href
    result = html.xpath('//li[last()]/a/@href')
    print(result)

    #7. 获取倒数第二个元素的内容
    result = html.xpath('//li[last()-1]/a')
    #text方法可以获取元素的内容
    print(result)
    print(result[0].text)

    #8. 获取 class 值为 bold 的标签名
    result = html.xpath('//*[@class="bold"]')
    print(result)
    #tag方法可以获取标签名
    print(result[0].tag)

print("华丽的分割线=========================================================================================")

#demo:
if __name__ == '__main__':
    html_str = """
        <div> <ul>
        <li class="item-1"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a>
        </ul> </div>

    """
    #1.转换成可解析的类型
    html_data = etree.HTML(html_str)
    #2.解析数据,使用xpath语法
    # result = html_data.xpath('//li')
    result = html_data.xpath('//li[1]')
    result1 = html_data.xpath('//a')

    #取出link3的标签a
    result2 = html_data.xpath('//li[@class="item-inactive"]/a/text()')
    result3 = html_data.xpath('//a[@href="link3.html"]/text()')
    #3.格式化
    all_data = etree.tostring(html_data)
    #返回的类型是列表
    print(result)
    print(result1)
    print(all_data.decode())
    print(result2)
    print(result3)




























