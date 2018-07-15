from bs4 import BeautifulSoup
import re
if __name__ == '__main__':
    """
    遍历文档树
    """

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
    # 创建 Beautiful Soup 对象
    soup = BeautifulSoup(html, 'lxml')

    """
    1. 直接子节点 ：.contents .children 属性
    """
    #.content:可以将tag的子节点以列表的方式输出
    print(soup.head.contents)
    # [<title>The Dormouse's story</title>]

    #可以用列表索引来获取它的某一个元素
    print(soup.head.contents[0])
    #<title>The Dormouse's story</title>

    #.children:它是一个 list 生成器对象,可以遍历获取子节点
    print(soup.head.children)
    #<list_iterator object at 0x7f9013ddedd8>
    for child in soup.body.children:
        print(child)

    """
    2. 所有子孙节点: .descendants 属性

    .contents 和 .children 属性仅包含tag的直接子节点，
    .descendants 属性可以对所有tag的子孙节点进行递归循环，
    和 children类似，我们也需要遍历获取其中的内容。
    """

    for child in soup.descendants:
        print(child)


    """
    3. 节点内容: .string 属性
    如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容。如果标签里面只有唯一的一个标签了，那么 .string 也会返回最里面的内容
    """
    print(soup.head.string)
    #The Dormouse's story

    print(soup.title.string)
    #The Dormouse's story



    """
    搜索文档树
    """
    """
    1.find_all(name, attrs, recursive, text, **kwargs)
    """
    #name参数:可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉
    #传字符串
    #在搜索方法中传入一个字符串参数,Beautiful Soup会查找与字符串完整匹配的内容
    print(soup.find_all('b'))
    # [<b>The Dormouse's story</b>]
    print(soup.find_all('a'))
    # [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
    # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    #传正则表达式
    #传入正则表达式作为参数,Beautiful Soup会通过正则表达式的 match() 来匹配内容
    for tag in soup.find_all(re.compile('^b')):
        print(tag.name)
        # body
        # b

    #传列表:传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回
    print(soup.find_all(['a','b']))
    #[<b>The Dormouse's story</b>, <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
    # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]


    #keyword参数:
    print(soup.find_all(id='link2'))
    #[<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

    #text参数:可以搜搜文档中的字符串内容，与 name 参数的可选值一样, text 参数接受 字符串 , 正则表达式 , 列表
    print(soup.find_all(text='Elsie'))

    print(soup.find_all(text=['Title', 'Elsie', 'Lacie']))

    print(soup.find_all(text=re.compile('Dormouse')))

    """
    2. CSS选择器
        写 CSS 时，标签名不加任何修饰，类名前加.，id名前加#
        可以利用类似的方法来筛选元素，用到的方法是 soup.select()，返回类型是 list
    """
    #（1）通过标签名查找
    print(soup.select('title'))
    print(soup.select('a'))
    print(soup.select('b'))
    #（2）通过类名查找
    print(soup.select('.sister'))
    #（3）通过 id 名查找
    print(soup.select('#link1'))
    #（4）组合查找:组合查找即和写 class 文件时，标签名与类名、id名进行的组合原理是一样的
    print(soup.select('p #link1'))
    #直接子标签查找，则使用 > 分隔
    print(soup.select('head > title'))
    #（5）属性查找:查找时还可以加入属性元素，属性需要用中括号括起来，注意属性和标签属于同一节点，所以中间不能加空格，否则会无法匹配到。
    print(soup.select('a[class="sister"]'))
    print(soup.select('a[href="http://example.com/elsie"]'))
    #同样，属性仍然可以与上述查找方式组合，不在同一节点的空格隔开，同一节点的不加空格
    print(soup.select('p a[href="http://example.com/elsie"]'))
    #(6) 获取内容
    #select 方法返回的结果都是列表形式，可以遍历形式输出，然后用 get_text() 方法来获取它的内容。
    soup = BeautifulSoup(html, 'lxml')
    print(type(soup.select('title')))
    print(soup.select('title')[0].get_text())

    for title in soup.select('title'):
        print(title.get_text())


#demo
if __name__ == '__main__':
    html_data = '''
        <html><head><title>The Dormouse's story</title></head>
        <body>
        <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>
        <p class="story">...</p>
    '''

    # 1 .转换类型
    soup = BeautifulSoup(html_data, 'lxml')

    # 2 . 解析标签 数据 find  find_all select

    # 3. find 符合条件的第一个标签
    result = soup.find(name='p')
    #属性里面也可以写多个
    result = soup.find(attrs={'id':"link2"})
    #文本搜索文本
    result = soup.find(text="...")
    #传正则
    pattern = re.compile('^a')
    result = soup.find(pattern)

    # 4. find_all 返回列表
    result = soup.find_all('a')

    # 5. select css选择器; 返回列表 list
    # 标签 类 ID  层级后代 组选择器 属性选择器
    result = soup.select('title')
    result = soup.select('.title')
    result = soup.select('#link3')
    result = soup.select('p a')
    result = soup.select('head,title')
    result = soup.select('a[id="link2"]')


    # 6. 找标签包裹的内容 get_text()
    result = soup.select('a[id="link2"]')[0].get_text()

    # 7. 属性  get('属性名称')
    result = soup.select('a[id="link2"]')[0].get('href')

    print(result)