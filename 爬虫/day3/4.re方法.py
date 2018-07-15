import re
"""
re模块的使用步骤:
    1.使用compile()函数将正则表达式的字符串形式编译成为一个pattern对象
    2.通过pattern对象提供的一系列方法对文本进行[匹配查找,获取匹配结果,一个Match对象
    3.最后使用match对象提供的属性和方法获取信息,根据需要进行其他操作
compile函数:
    compile函数用于编译正则表达式,生成Pattern对象
        import re
        # 将正则表达式编译成 Pattern 对象
        pattern = re.compile(r'\d+')
    之后我们可以利用pattern的一系列方法对文本进行匹配查找
    match 方法：从起始位置开始查找，一次匹配
    search 方法：从任何位置开始查找，一次匹配
    findall 方法：全部匹配，返回列表
    finditer 方法：全部匹配，返回迭代器
    split 方法：分割字符串，返回列表
    sub 方法：替换


"""
"""
1.match方法:用于查找字符串的头部(也可以指定起始位置),
            它是一次匹配,只要找到了一个匹配的结果就返回,
            而不是查找所有匹配的结果,
使用格式:match(string[, pos[, endpos]])
            string是待匹配的字符串,pos和endpos是可选参数,指定字符串的起始和终点位置,
            默认值分别是0和len(字符串长度),所以当我们不指定pos和endpos时,match方法默认匹配字符串的头部
            当匹配成功的时候,返回match,如果没有匹配上,返回的None
"""
#demo1:匹配至少一个数字
if __name__ == '__main__':
    #用于匹配至少一个数字
    pattern = re.compile(r'\d+')
    #查找头部
    m = pattern.match('one12twothree34four')
    #没有匹配,返回None
    print(m)

    #从e的位置开始匹配,
    n = pattern.match('one12twothree34four', 2, 10)
    #没有匹配结果,返回None
    print(n)

    #从1的位置开始匹配
    g = pattern.match('one12twothree34four', 3, 10)
    #正好由匹配结果,返回一个match对象 <_sre.SRE_Match object; span=(3, 5), match='12'>
    print(g)
    print(g.group())
    print(g.start())
    print(g.end())
    print(g.span())

    """
    当匹配成功返回一个match对象:
        1.group([group1, …])方法用于获得一个或多个分组匹配的字符串,当要获得整个匹配的子串时
        可以使用group()或者group(0) ,此处0可以省略
        2.start()方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引）,参数默认值为0
        3.end()方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1）,参数默认值为0
        4.span()方法返回(sart(), end())

    """
#demo2:
if __name__ == '__main__':
    pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)  # re.I 表示忽略大小写
    m = pattern.match("Hello World Wide Web")
    #匹配成功返回一个match对象
    print(m)
    # 返回匹配成功的整个子串
    print(m.group())
    # 返回匹配成功的整个子串的索引
    print(m.span())
    # 返回第一个分组匹配成功的子串的索引
    print(m.span(1))
    # 返回第二个分组匹配成功的子串的索引
    print(m.span(2))
    # 返回第一个分组匹配成功的子串
    print(m.group(1))
    # 返回第二个分组匹配成功的子串
    print(m.group(2))
    # 等价于 (m.group(1), m.group(2), ...)
    print(m.groups())

"""
2.search方法:用于查找字符串的任何位置,也是匹配一次,只要找到了一个匹配的结果就返回,而不是查找所有匹配的结果
    使用形式:search(string[, pos[, endpos]])
            string 是待匹配的字符串，pos 和 endpos 是可选参数，指定字符串的起始和终点位置，默认值分别是 0 和 len (字符串长度)。
            当匹配成功时，返回一个 Match 对象，如果没有匹配上，则返回 None。
"""
#demo1:用search查询至少匹配一个数字
if __name__ == '__main__':
    pattern = re.compile('\d+')
    m = pattern.search('one12twothree34four')  # 这里如果使用 match 方法则不匹配
    #<_sre.SRE_Match object; span=(3, 5), match='12'>
    print(m)
    #12
    print(m.group())
    m = pattern.search('one12twothree34four', 10, 30)  # 指定字符串区间
    #34
    print(m.group())
    #(13, 15)
    print(m.span())


#demo2:查询匹配结果并打印匹配的位置
if __name__ == '__main__':
    pattern = re.compile(r'\d+')
    # 使用 search() 查找匹配的子串，不存在匹配的子串时将返回 None
    # 这里使用 match() 无法成功匹配
    m = pattern.search('hello 123456 789')
    if m:
        #使用match获得分组信息 123456
        print('matching string:', m.group())
        #起始位置和结束位置 (6, 12)
        print('position:', m.span())

"""
3.findall方法:获得所有匹配的结果
        使用方法:findall(string[, pos[, endpos]])
        string 是待匹配的字符串，pos 和 endpos 是可选参数，指定字符串的起始和终点位置，默认值分别是 0 和 len (字符串长度)。
        findall 以列表形式返回全部能匹配的子串，如果没有匹配，则返回一个空列表。

"""
#demo1:查找数字
if __name__ == '__main__':
    pattern = re.compile(r'\d+')   # 查找数字
    result1 = pattern.findall('hello 123456 789')
    result2 = pattern.findall('one1two2three3four4', 0, 10)
    #['123456', '789']
    print(result1)
    #['1', '2']
    print(result2)

#demo2:查找匹配小数
if __name__ == '__main__':
    # re模块提供一个方法叫compile模块，提供我们输入一个匹配的规则
    # 然后返回一个pattern实例，我们根据这个规则去匹配字符串
    pattern = re.compile(r'\d+\.\d*')
    # 通过partten.findall()方法就能够全部匹配到我们得到的字符串
    result = pattern.findall("123.141593, 'bigcat', 232312, 3.15")
    # findall 以 列表形式 返回全部能匹配的子串给result,遍历
    for item in result:
        print(item)


"""
3.finditer方法:跟 findall 的行为类似，也是搜索整个字符串，获得所有匹配的结果。但它返回一个顺序访问每一个匹配结果（Match 对象）的迭代器。

"""
#demo
if __name__ == '__main__':
    pattern = re.compile(r'\d+')
    result_iter1 = pattern.finditer('hello 123456 789')
    result_iter2 = pattern.finditer('one1two2three3four4', 0, 10)
    print(type(result_iter1))
    print(type(result_iter2))
    print("result_iter1的结果....")
    for m1 in result_iter1:
        print("matching string:{}, position:{}".format(m1.group(), m1.span()) )
    print("result_iter2的结果....")
    for m2 in result_iter2:
        print("matching string:{}, position:{}".format(m2.group(), m2.span()))


"""
4.split方法:按着能够匹配的子串将字符串分割后返回列表
        使用形式:split(string[, maxsplit])  maxsplit 用于指定最大分割次数，不指定将全部分割。

"""
#demo
if __name__ == '__main__':
    p = re.compile(r'[\s\,\;]+')
    #['a', 'b', 'c', 'd']
    print(p.split('a,b;; c   d'))

"""
5.sub方法:用于替换, 使用形式sub(repl, string[, count])   repl 可以是字符串也可以是一个函数
        如果repl是字符串,则会使用repl去替换字符串每一个匹配的子串,并返回替换后的字符串,repl 还可以使用 id 的形式来引用分组，但不能使用编号 0
        如果 repl 是函数，这个方法应当只接受一个参数（Match 对象），并返回一个字符串用于替换（返回的字符串中不能再引用分组）。
        count 用于指定最多替换次数，不指定时全部替换。
"""
#demo
if __name__ == '__main__':
    p = re.compile(r'(\w+) (\w+)')    # \w = [A-Za-z0-9_]
    s = 'hello 123, hello 456'
    # 使用 'hello world' 替换 'hello 123' 和 'hello 456'
    print(p.sub(r'hello world', s))
    print(p.sub(r'\2 \1', s))   #引用分组

    def func(m):
        return  'hi' + '' + m.group(2)
    print(p.sub(func, s))
    #最多替换一次
    print(p.sub(func,s,1))


"""
6.匹配中文: 在某些情况下，我们想匹配文本中的汉字，有一点需要注意的是，
            中文的 unicode 编码范围 主要在 [u4e00-u9fa5]，这里说主要是因为这个范围并不完整，比如没有包括全角（中文）标点，不过，在大部分情况下，应该是够用的。

"""
#demo:
if __name__ == '__main__':
    title = "你好,hello,世界"
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    result = pattern.findall(title)
    print(result)

"""
7.贪婪模式与非贪婪模式:
    贪婪模式：在整个表达式匹配成功的前提下，尽可能多的匹配 ( * )；
    非贪婪模式：在整个表达式匹配成功的前提下，尽可能少的匹配 ( ? )；
示例1:源字符串：abbbc
    使用贪婪的数量词的正则表达式 ab* ，匹配结果： abbb。
    * 决定了尽可能多匹配 b，所以a后面所有的 b 都出现了。

    使用非贪婪的数量词的正则表达式ab*?，匹配结果： a。
    即使前面有 *，但是 ? 决定了尽可能少匹配 b，所以没有 b。

示例2:源字符串：aa<div>test1</div>bb<div>test2</div>cc
    使用贪婪的数量词的正则表达式：<div>.*</div>
    匹配结果：<div>test1</div>bb<div>test2</div>
    解释:这里采用的是贪婪模式。在匹配到第一个“</div>”时已经可以使整个表达式匹配成功，但是由于采用的是贪婪模式，所以仍然要向右尝试匹配，
        查看是否还有更长的可以成功匹配的子串。匹配到第二个“</div>”后，向右再没有可以成功匹配的子串，匹配结束，匹配结果为“<div>test1</div>bb<div>test2</div>”
    使用非贪婪的数量词的正则表达式：<div>.*?</div>
    匹配结果：<div>test1</div>
    正则表达式二采用的是非贪婪模式，在匹配到第一个“</div>”时使整个表达式匹配成功，由于采用的是非贪婪模式，所以结束匹配，不再向右尝试，匹配结果为“<div>test1</div>”。
"""

if __name__ == '__main__':
    #.* 匹配换行 re.S
    str_one = """
            asfsdsdffdsb
            fsdjfdjfdsjk
            fsdsfdfdfdsB
        """
    #1.创建正则对象 .* 匹配换行符,由于换行了所以值匹配到['sfsdsdffds']
    #默认就是贪婪模式
    patter = re.compile('a(.*)b')

    #加dotall表示可以匹配换行的
    patter = re.compile('a(.*)b', re.DOTALL)

    #re.DOALL和re.S是一样的,都是为了匹配换行以后的内容
    patter = re.compile('a(.*)b', re.S)

    # #2.忽略大小写,两个修饰中间用竖线隔开 I就是IGNORECASE
    patter = re.compile('a(.*)b', re.S | re.I)

    #findall
    result = patter.findall(str_one)
    print(result)

    #3.原始字符串
    #前面不加r就显示a  b
    str_two = 'a\nb'
    #加上r保留原始字符串
    str_two = r'a\nb'
    print(str_two)

    #不加r的话就默认删除了n前面的内容,只显示n
    str_thre = 'a\bn'
    #加上r保存原始字符串
    str_thre = r'a\bn'
    print(str_thre)