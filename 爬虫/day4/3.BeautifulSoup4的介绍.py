"""
1.什么是BeautifulSoup4?
    和 lxml 一样，Beautiful Soup 也是一个HTML/XML的解析器，主要的功能也是如何解析和提取 HTML/XML 数据。
    lxml 只会局部遍历，而Beautiful Soup 是基于HTML DOM的，会载入整个文档，解析整个DOM树，因此时间和内存开销都会大很多，所以性能要低于lxml。
    BeautifulSoup 用来解析 HTML 比较简单，API非常人性化，支持CSS选择器、Python标准库中的HTML解析器，也支持 lxml 的 XML解析器。

2.BeautifulSoup四个对象种类
    Tag  :通俗点讲就是 HTML 中的一个个标签
            title head a p等等 HTML 标签加上里面包括的内容就是 Tag
            '''
            <head><title>The Dormouse's story</title></head>
            <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
            <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
            '''
    NavigableString :既然我们已经得到了标签的内容,我们要想获取标签内部的文字
    BeautifulSoup :表示的是一个文档的内容。大部分时候,可以把它当作 Tag 对象，是一个特殊的 Tag，我们可以分别获取它的类型，名称，以及属性来感受一下
    Comment  :对象是一个特殊类型的 NavigableString 对象，其输出的内容不包括注释符号。

"""
#demo1:bs4的基本使用
from bs4 import BeautifulSoup

if __name__ == '__main__':
    html = """
        <html><head><title>The Dormouse's story</title></head>
        <body>
        <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>
        <p class="story">...</p>

    """
    #创建BeautifulSoup对象
    soup = BeautifulSoup(html, 'lxml')

    #打开本地HTMl文件的方式来创建对象
    # soup = BeautifulSoup(open('index.html'))

    #格式化输出soup对象的内容
    print(soup.prettify())


#demo2:四大对象的使用,了解

if __name__ == '__main__':
    html = """
        <html><head><title>The Dormouse's story</title></head>
        <body>
        <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>
        <p class="story">...</p>

    """
    # 1.Tag:

    #创建BeautifulSoup对象
    soup = BeautifulSoup(html, 'lxml')
    print(soup.title)
    # <title>The Dormouse's story</title>

    print(soup.head)
    # <head><title>The Dormouse's story</title></head>

    print(soup.a)
    # <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>

    print(soup.a)
    # <p class="title" name="dromouse"><b>The Dormouse's story</b></p>

    print(type(soup.p))
    # <class 'bs4.element.Tag'>

    #总结:
    #我们可以利用 soup 加标签名轻松地获取这些标签的内容，这些对象的类型是bs4.element.Tag。
    # 但是注意，它查找的是在所有内容中的第一个符合要求的标签。如果要查询所有的标签，后面会进行介绍。


    #对于 Tag，它有两个重要的属性，是 name 和 attrs

    print(soup.name)
    # [document] #soup 对象本身比较特殊，它的 name 即为 [document]

    print(soup.head.name)
    # head 对于其他内部标签，输出的值便为标签本身的名称

    print(soup.p.attrs)
    # {'class': ['title'], 'name': 'dromouse'}
    # 在这里，我们把 p 标签的所有属性打印输出了出来，得到的类型是一个字典。

    print(soup.p['class']) # soup.p.get('class')
    # ['title'] #还可以利用get方法，传入属性的名称，二者是等价的

    soup.p['class'] = 'newClass'  # 可以对这些属性和内容等等进行修改
    print(soup.p)
    # <p class="newClass" name="dromouse"><b>The Dormouse's story</b></p>

    del soup.p['class']  # 还可以对这个属性进行删除
    print(soup.p)
    # <p name="dromouse"><b>The Dormouse's story</b></p>


    #2. NavigableString
    print(soup.p.string)
    # The Dormouse's story

    print(type(soup.p.string))
    # In [13]: <class 'bs4.element.NavigableString'>

    #3. BeautifulSoup
    print(type(soup.name))
    print(soup.attrs) # 文档本身的属性为空

    #4. Comment
    print(soup.a)
    # <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>

    print(soup.a.string)
    # Elsie

    print(type(soup.a.string))
    # <class 'bs4.element.Comment'>



















