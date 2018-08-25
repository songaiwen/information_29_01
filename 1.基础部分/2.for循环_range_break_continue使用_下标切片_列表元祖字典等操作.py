#第三 :for循环,range使用,字符串定义,输出和输入,下标,切片,操作字符串,列表循环和增删改查

#1.for 循环： 遍历对象依次获取对象的每一个值，比如：可以遍历：字符串，列表，元组，字典，集合，range等
# 定义遍历的字符串
"""
for 临时变量 in 列表或者字符串等可迭代对象:
    循环满足条件时执行的代码

"""
my_str = "hello"

# 还可以根据下标获取字符串中的某个字符
print(my_str[0])
for value in my_str:
    print(value)
for result in my_str:
    if result == "l":
        print("l 过来了")
    print(result)

#2.range的使用
#创建范围对象
result = range(3)
print(result)
#需求:通过循环验证范围是否包含结束的位置
# range(3): => [0,3), 如果只传入一个参数，那么开始位置是从0开始
for value in result:
    print(value)
#需求:创建范围对象,1到3,但是不包含3 [1,3)
result = range(1, 3)
for value in result:
    print(result)
#需求:参数1开始位置,参数2结束位置的前一个,参数三,步长,如果是正数,每次取下一个值,加上步长就可以了
result = range(1,11,2)
for value in result:
    print(value)
#需求:如果步长是负数,那么加上步长的时候其实是加上一个负的步长
result = range(5,0,-1)
for value in result:
    print(value)

#3.break 和continue的使用方法:只能在循环语句(for和while)里面使用
# break: 立即结束break所在的循环，执行到break后面的代码不会执行
# continue: 立即结束本次循环，然后可以再次循环下一次， 执行到continue后面的代码不执行
"""
for value in "hello":
    if value == "l":
        # 代码执行到break，break所在的循环立即结束，后面的代码不执行
        break
    print(value)

"""
"""
for value in "hello":
    if value == "l":
        # 代码执行到continue，结束本次循环，然后执行下一次循环，continue后面的代码不执行
        continue

    print(value)
"""
# 扩展
"""
#for循环还可以结合else语句使用
    for value in "hi python":
        print(value)
    else:
        print("循环结束")
"""
"""
for value in "hi python":
    if value == "i":
        break
    print(value)
else:
    # 注意点: 只要循环语句执行break，那么else语句不执行，否则else语句执行
    print("循环结束")
"""
"""
for value in "hi python":
    if value == "i":
        continue
    print(value)
else:
    # 注意点： 循环语句里面执行continue，那么else语句还可以执行
    # 总结： 只要循环不执行break，那么else语句就执行
    print("循环结束")
"""
"""
行数
row = 1

while row <= 3:
    if row == 2:
        # 代码执行到break，break所在的循环立即结束，后面的代码不执行
        break
    print(row)
    row += 1
"""
"""
row = 1
while row <= 3:
    if row == 2:
        # 代码执行到break，break所在的循环立即结束，后面的代码不执行
        print("我本次循环结束，再次执行下一次循环")
        row += 1
        # 代码执行到continue，结束本次循环，然后执行下一次循环，continue后面的代码不执行
        continue
    print(row)
    row += 1
"""
"""
row = 1
while row <= 3:
    if row == 2:
        # break
        row += 1
        continue
    print(row)
    row += 1
else:
    # 总结： 只要循环不执行break，那么else语句就执行
    print("循环结束")

"""
#总结:break/continue只能用在循环中，除此以外不能单独使用
#break/continue在嵌套循环中，只对最近的一层循环起作用


#4.字符串的定义格式由四种,使用单引号或者双引号或者三引号包起来的数据就是字符串
my_str1 = 'hi "xx" python'
my_str2 = "您好，'yyy' python"
my_str3 = '''
    哈哈，我是多行字符串
    哈哈，我是多行字符串
    哈哈，我是多行字符串
    'hehehe'  "水电费浮点数水电费"
'''
my_str4 = """
    哈哈，我是多行字符串
    哈哈，我是多行字符串
    哈哈，我是多行字符串
    'hehehe'  "水电费浮点数水电费"
"""

#5.下标(索引):通俗理解为一个编号,根据下标或者索引获取对应的数据,可以通过下表获取数据的对象有:字符串,列表,元祖
#例如:超市储物柜
#列表与元组支持下标索引好理解，字符串实际上就是字符的数组，所以也支持下标索引。
#注意python中下标从 0 开始
my_str = "hello"
# 获取第一个元素
result = my_str[0]
print(result)
# 获取最后一个元素的两种方法
result = my_str[4]
print(result)
result = my_str[-1]
print(result)
#需求:通过下表来遍历数据
#开始下标
start_index = 0
#获取字符串的长度,len函数获取字符串的长度
my_str_len = len(my_str)
#计算最大的下标
max_index = my_str_len - 1
#如果开始下标小于最大的下标
while start_index <= max_index:
    #得到相应的下标
    result = my_str[start_index]
    print(result)
    #每循环一次下标加1
    start_index += 1


#6.切片:获取对象中其中一部分数据,[开始索引:结束索引:步长],适用于字符串,列表和元祖
#注意：选取的区间从"起始"位开始，到"结束"位的前一位结束（不包含结束位本身)，步长表示选取间隔。
# 索引是通过下标取某一个元素
# 切片是通过下标去某一段元素

my_str = "songyuxi"
#获取指定切片数据
result = my_str[0:3]
print(result)  #--------------->son
result = my_str[1:4]
print(result)  #--------------->ong
#获取整个字符串,两种方法
result = my_str[0:8]
print(result)
result = my_str[:]
print(result)
#表示步长
result = my_str[0:8:2]
print(result)  #------------>snyx
result = my_str[::2]
print(result)  #------------>snyx
#获取前三个的快捷方式
result = my_str[:3]
print(result)  #------------>son
#获取后三个快捷方式
result = my_str[-3:]
print(result)  #------------>uxi
#注意点:开始索引如果小于结束索引,步长为正数,否则为负数
my_str1 = "zhuzhihui"
result = my_str1[1:4:1]
print(result)   #---------->huz
result = my_str1[7:0:-1]
print(result)   #---------->uhihzuh
#扩展:面试题
s = 'Hello World!'
print(s[4])  #------------------------------->o
# 取出所有元素（没有起始位和结束位之分），默认步长为1
print(s[:])    #------------------------------->Hello World!
# 从下标为1开始，取出 后面所有的元素（没有结束位）
print(s[1:])   #------------------------------->ello World!
# 从起始位置开始，取到 下标为5的前一个元素（不包括结束位本身）
print(s[:5])   #------------------------------->Hello
# 从起始位置开始，取到 倒数第一个元素（不包括结束位本身）
print(s[:-1])  #------------------------------->Hello World
# 从倒数第4个元素开始，取到 倒数第1个元素（不包括结束位本身）
print(s[-4:-1])  #------------------------------->rld
# 从下标为1开始，取到下标为5的前一个元素，步长为2（不包括结束位本身）
print(s[1:5:2])  #------------------------------->el
# python 字符串快速逆置
print(s[::-1])  # 从后向前，按步长为1进行取值  !dlroW olleH


#7.字符串常见操作
my_str = "hello"
# find: 根据指定字符串获取对应的下标
# 默认find是从左往右找， rfind: 从右往左找
result = my_str.find("l")
result1 = my_str.rfind("l")
print(result, result1)
# 还可以根据指定范围去找到指定字符串的下标
# 扩展:
# 参数1: 指定查找的字符串
# 参数2: 开始索引
# 参数3： 结束索引， 不包含结束索引,找不到的话返回-1,代表没有找到
result = my_str.find("e", 0, 1)
print(result)
# index: 根据指定字符串获取对应的下标 , 找不到崩溃
# result = my_str.index("f")
# print(result)

# count:统计指定字符串出现次数
# 还可以指定范围，但是不包含结束索引
result = my_str.count("l", 0, 3)
print(result)

# replace: 根据指定字符串进行替换
# 1: 表示替换的次数
result = my_str.replace("l", "w", 1)
print(result)

# 需求:定义水果字符串
my_fruit = "鸭梨,葡萄,橙子,菠萝"
# split: 根据指定字符串分割数据返回列表数据类型
# 1: 表示分割的次数
result = my_fruit.split(",", 1)
print(result)
#需求:给定一个字符串,返回使用空格或者\t分割后的字符串
testStr = "haha nihao a \t heihei \t woshi nide \t hao \npengyou"
result = testStr.split()
print(result)

# 定义网址
my_url = "http://www.baidu.comxx"
# startswith： 判断是否是以指定字符串开头
result = my_url.startswith("http")
print(result)
# endswith： 判断是否是以指定字符串结尾
result = my_url.endswith(".com")
print(result)

my_desc = "ok"
# ljust： 在指定字符串的长度内居左显示，长度不够使用空格
result = my_desc.ljust(5)
print(result)
result = my_desc.rjust(5)
print(result)
result = my_desc.center(5)
print(result)

# lstrip()；默认去除左边空格
my_str1 = "  哈哈"
result = my_str1.lstrip()
print(result)

my_str1 = "xx哈哈"
# 根据指定字符串删除指定字符
result = my_str1.lstrip("x")
print(result)
my_str2 = "ffdddd"
result = my_str2.rstrip("d")
print(result)

# 默认去除两边空格
my_str3 = "  嘻嘻  "
result = my_str3.strip()
print(result)

# 扩展:
# 根据指定字符串删除
my_str3 = "ff嘻嘻ff"
result = my_str3.strip("ff")
print(result)

# join 把标记字符串加入到指定对象里面
my_str = "hello"
flag_str = ","
# 把标记字符串加入到指定对象里面
result = flag_str.join(my_str)
print(result)


#8. 字符串拼接
result = "hello" + "world"
print(result)
# 列表合并
result = [1,2,] + [3,4]
print(result)
result = (5,6) + (7,8)
print(result)
# 复制
result = "A" * 5
print(result)
result = [12, 36] * 3
print(result)
result = ("星星", "月亮") * 4
print(result)
# in 判断参数是否在指定对象里面
result = "a" in "add"
print(result)


#9.列表的介绍:以中括号表现存储数据的集合 比如: [3,5,7]
#比C语言的数组强大的地方在于列表中的元素可以是不同类型的
my_list = ["鸭梨", "西瓜", "椰子"]
print(my_list)

# 在python里面可以在列表里面放入任意类型数据
my_list = [3, 5, "哈哈", "嘻嘻"]
print(my_list)
# 根据下标获取列表中对应的元素
result = my_list[0]
print(result)
# 获取最后一个元素
result = my_list[-1]
print(result)
# 通过切片获取一部分元素
result = my_list[0:2]
print(result)


#10.列表的循环
my_list = ["杨幂", "杨钰莹", "高圆圆"]
# 使用for循环遍历列表中每一个数据
for value in my_list:
    print(value)
print("---------------")
# while循环遍历列表
# 开始下标
start_index = 0
# 结束下标  len(): 可以列表长度，元素的个数， 还可以获取字符串的长度
end_index = len(my_list) - 1
while start_index <= end_index:
    result = my_list[start_index]
    print(result)
    start_index += 1

#11.列表的增删改查
# 定义列表:<1>添加元素("增"append, extend, insert)
my_list = []  # list()
# 添加(追加)数据 =》append
my_list.append("小明")
my_list.append("小红")
# 插入 insert  insert(index, object) 在指定位置index前插入元素object
my_list.insert(1, "小丽")
print(my_list)
# 名字列表
name_list = ["小花", "小婉"]
my_list.append(name_list)
print(my_list)

# extend: 扩展，把列表中的每一个元素拆开放到对应的列表里面
my_list.extend(name_list)
print(my_list)

# 修改:修改元素的时候，要通过下标来确定要修改的是哪个元素，然后才能进行修改
my_list[1] = "小白"
print(my_list)
# 扩展： 通过切片修改多个值
my_list[0:2] = ["小李", "小王"]
print(my_list)

# 删除
# remove： 根据指定元素删除列表中的元素
my_list.remove("小王")
print(my_list)
# del 根据下标删除
# del my_list[0]
# print(my_list)
# 删除多个，可以根据切片
del my_list[0:2]
print(my_list)
# pop删除，默认删除最后一个元素, 注意会返回删除的元素
result = my_list.pop()
print(result)
print(my_list)

my_list = ["小李", "小郭", "小王"]
# 扩展： pop可以根据指定下标删除
result = my_list.pop(1)
print(result)
print(my_list)

# 查询 in   <3>查找元素("查"in, not in, index, count)
# in 根据指定元素判断列表里面是否有对应的元素，如果有返回True，否则是Flase
result = "小李" in my_list
print(result)
result = "小郭" not in my_list
print(result)


#12.列表的补充
# index: 根据指定的字符串获取列表中元素对应的下标
my_list = ["小花", "小婉", "小娜", "小婉"]
# index: 根据指定的字符串获取列表中元素对应的下标
result = my_list.index("小婉")
print(result)

# count： 统计指定元素在列表中出现的个数
count = my_list.count("小婉")
print(count)

# 排序:<5>排序(sort, reverse)
my_list = [3, 6, 1, 2]
# 列表的反转
my_list.reverse()
print(my_list)

# sort表示排序， 默认是升序
my_list.sort()
print(my_list)
# 降序： 先排序然后反转就可以完成降序
my_list.sort(reverse=True)
print(my_list)

#扩展:大小写的应用场景
while True:
    print('请输入信息')
    input("请输入您的姓名:")

    confirmeQuit = input('退出?yes  or no')
    confirmeQuit = confirmeQuit.lower()
    if confirmeQuit == "yes":
        break

#需求:使用列表写一个简单的名字管理系统

allNames = []
while True:
    print("-"*30)
    print("1: 添加新名字")
    print("2: 修改名字")
    print("3: 删除名字")
    print("4: 设置显示时的排序方式")
    print("5: 显示所有的名字")
    print("6: 退出系统")
    print("7: 查询指定名字的个数")
    print("-"*30)

    op = input("请输入用能对应的数字:")

    # allNames = []
    if op == "1":
        # allNames = []
        newName = input("请输入新的名字:")
        # if allNames.count(newName) == 0:
        if newName not in allNames:
            allNames.append(newName)
        else:
            print("该名字已经存在,请重新输入")
    elif op == "2":
        modifyNum = int(input("请输入要修改的名字对应的序号"))
        modifyName = input("请输入新的名字:")
        allNames[modifyNum - 1] = modifyName
    elif op == "3":
        delId = int(input("请输入要删除的序号:"))
        confimeDel = input("确定? yes  or  no")
        confimeDel = confimeDel.lower()
        if confimeDel == "yes":
            del allNames[delId - 1]

    elif op == "4":
        sortNum = input("1:从小到大排序, 2:从大到小排序")
        if sortNum == "1":
            allNames.sort()  # 从小到大排序
        elif sortNum == "2":
            allNames.sort(reverse=True)  # 从大到小排序
    elif op == "5":
        print("=" * 40)
        print("id\tname")
        i = 1
        for name in allNames:
            print("%d\t%s" % (i, name))
            i += 1
    elif op == "6":
        print("=" * 30)
        print("这里是退出功能")
        break
    elif op == "7":
        countName = input("请输入要查询的名字:")
        countNum = allNames.count(countName)
        print("%s的个数是:%d" % (countName, countNum))
    else:
        print("您的输入有误,请重新输入")


#需求:家庭成员管理小系统
# 分析:
# 1. 要存储几个人的信息?---->好像应该使用列表来存储多个数据
# 2. 每个人的信息都有些什么呢?----->好像应该使用字典来存储个人信息
'''
myInfo = {"name":"dongge", "id":"3713xxxxxxxxxx", "marry":"是"}
myWifeInfo = {"name":"dongSao", "id":"3713xxxxxxxxxx", "marry":"是"}

homeInfo = []
homeInfo.append(myInfo)
homeInfo.append(myWifeInfo)
'''

homeInfo = []

while True:
    print("-" * 30)
    print("1:添加家庭成员")
    print("2:显示家庭成员")
    print("3:退出系统")
    print("-" * 30)

    op = input("请输入要进行的功能选项:")

    if op == "1":
        # 添加一个新的家庭成员
        name = input("请输入姓名:")
        sex = input("请输入性别:")
        cardId = input("请输入id:")
        marry = input("请输入是否已婚:")

        newInfo = {}
        newInfo['name'] = name
        newInfo['sex'] = sex
        newInfo['cardId'] = cardId
        newInfo['marry'] = marry

        homeInfo.append(newInfo)

    elif op == "2":
        print("=" * 40)
        print("id\tname\tsex\tmarry")
        for personInfo in homeInfo:
            print("%s\t" % personInfo['cardId'], end="")
            print("%s\t" % personInfo['name'], end="")
            print("%s\t" % personInfo['sex'], end="")
            print("%s\t" % personInfo['marry'])
    elif op == "3":
        break



#第四:列表嵌套,元祖,字典增删改查和遍历,几种数据类型使用的公共方法
#1.列表的嵌套:在列表里面再使用一个列表就是列表的嵌套比如 : [[yyy], [xxx]]# 北方城市列表
north_city = ["北京", "天津"]
# 南方城市列表
south_city = ["广州", "深圳"]
# 城市列表
# city_list = [north_city, south_city]
city_list = [["北京", "天津"], ["广州", "深圳"]]
# 获取南方城市列表
result = city_list[1]
print(result)
# 获取南方城市列表里面的深圳城市
city_name = result[1]
print(city_name)
# 简洁方式
result = city_list[1][1]
print(result)

#需求:一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配
# 思路1
# 1.定义三个办公室， 2. 遍历老师，每次取到一个老师产生一个随机数字，然后根据随机数字判断放入到那个办公室
# office1 = []
# office2 = []
# office3 = []
# 思路2，使用列表嵌套
import random
office_list = [[], [], []]
# 定义老师列表
teacher_list = ["张老师", "李老师", "郭老师", "闫老师", "彭老师", "周老师", "王老师", "赵老师"]
# 遍历老师，随机产生下标[0-2]
for teacher in teacher_list:
    # 随机产生的下标
    index = random.randint(0, 2)
    # 根据下标获取对应的办公室
    office = office_list[index]
    # 把老师添加到指定的办公室
    office.append(teacher)

# 输出显示办公室的老师
print(office_list)

# num = 1
# # 遍历办公室列表
# for office in office_list:
#     # 获取人数
#     count = len(office)
#     print("办公室%d 有%d人" % (num, count))
#     # 遍历办公室列表，循环显示老师信息
#     for teacher in office:
#         # print(teacher,"", end="")
#         print("%s " % teacher, end="")
#     # 换行输出下一个办公室老师信息
#     print("")
#     if num != len(office_list):
#         print("-------------------")
#     # 循环依次，办公室编号加1
#     num += 1

# 遍历办公室列表
for index, office in enumerate(office_list):
    # 获取人数
    count = len(office)
    print("办公室%d 有%d人" % (index + 1, count))
    # 遍历办公室列表，循环显示老师信息
    for teacher in office:
        # print(teacher,"", end="")
        print("%s " % teacher, end="")
    # 换行输出下一个办公室老师信息
    print("")
    if index + 1 != len(office_list):
        print("-------------------")
    # 循环依次，办公室编号加1


#2.元祖:以小括号表现形式的数据集合就是元祖,元祖中的元素不能进行修改
#定义元祖
my_tuple = (3,5,7)
print(my_tuple, type(my_tuple))
# 如果元组里面只有一个元素，那么元组中的元素后面需要加上逗号，比如， (3,)
my_tuple = (3, )
print(my_tuple, type(my_tuple))
#定义一个水果的元祖,做下面的实例
fruit_tuple = ("鸭梨", "柚子", "草莓", "柚子")
# 根据下标获取元组中的元素
result = fruit_tuple[1]
print(result)
# 通过切片获取前面两个元素
result = fruit_tuple[0: 2]
print(result)
# 根据元素获取对应的下标
index = fruit_tuple.index("草莓")
print(index)
# 根据指定字符串获取元组中元素的个数
count = fruit_tuple.count("柚子")
print(count)
# for 遍历元组
for value in fruit_tuple:
    print(value)
# 以后再做开发的时候，不想外界修改返回的值，那么可以使用元组
fruit_tuple = ("鸭梨", "柚子", "草莓", "柚子", [2, 4, 6])
# 获取最后一个元素
result = fruit_tuple[-1]
result[2] = 7
print(result)
print(fruit_tuple)
# 注意点：不要直接修改元组中某个元素
# fruit_tuple[-1] = [1, 2, 3]


#3.字典:以key ,value表现形式的数据结合,比如:{"name": "zhangsan", ....}, 字典是无序， 字符串，列表，元组有序
# 字典和列表一样，也能够存储多个数据
# 列表中找某个元素时，是根据下标进行的
# 字典中找某个元素时，是根据'名字'（就是冒号:前面的那个值，例如上面代码中的'name'、'id'、'sex'）
# 字典的每个元素由2部分组成，键:值。例如 'name':'班长' ,'name'为键，'班长'为值
student_dict = {"age": 18, "name": "宋雨希", "address": "北京", "sex": "女"}
print(student_dict)
# 根据key获取对应的value
value = student_dict["name"]
print(value)
# 注意点: 使用中括号根据key获取对应的value的时候如果key不存在那么会崩溃
# score = student_dict["score"]
# print(score)

# get通过key获取对应的value
# age = student_dict.get("age")
# print(age)

# None：表示没有值，不等于空字符串， 代码不会崩溃， 还可以设置默认值
# score = student_dict.get("score")
# print(score)
# 如果key存在使用对应的value值，否则使用默认值
score = student_dict.get("score", 100)
print(score)

# 需求:字典的增删改查
# 人员信息字典
person_dict = {"name": "李广", "age": 20, "sex": "男"}
# 修改: 只有key存在，下面的代码是修改
person_dict["age"] = 22
print(person_dict)
# 如果key不存在，那么下面的代码是添加键值对
person_dict["address"] = "河北"
print(person_dict)

# 删除
# del person_dict["sex"]
# print(person_dict)

# 随机删除字典中键值对
person_dict.popitem()
print(person_dict)

# 查询key是否在指定的字典里面
result = "age" in person_dict   #=> person_dict.keys()
print(result)

# 判断value是否在字典里面
result = "李广" not in person_dict.values()
print(result)

# 清空字典
person_dict.clear()
print(person_dict)

# 清空列表
num_list = [1,24,5]
num_list.clear()
print(num_list)

#需求:字典的常见操作
my_dict =  {"name": "李广", "age": 20, "sex": "男"}
# len： 获取键值对的个数
count = len(my_dict)
print(count)
# keys: 获取字典中所有的key
keys = my_dict.keys()
# python3 里面keys需要通过list转换获取列表
print(list(keys))
# values: 获取字典中所有的value
values = my_dict.values()
print(list(values))
# items 获取字典中每项键值对，封装到元组里面
items = my_dict.items()
print(list(items))

#需求字典的遍历:通过for ... in ... 我们可以遍历字符串、列表、元组、字典等
my_dict = {"name": "李广", "age": 20, "sex": "男"}
# 默认遍历字典获取的每一个key
for key in my_dict:
    # 根据key获取对应的value
    value = my_dict[key]
    print(key, value)

# 遍历所有的value值
for value in my_dict.values():
    print(value)

# 遍历所有的key
for key in my_dict.keys():
    print(key)

# 遍历每项数据获取对应的key，value
for item in my_dict.items():
    print(item[0], item[1])

# 拆包获取元组里面的数据
for key, value in my_dict.items():
    print(key, value)

# enumerate函数，获取对象中成员下标和成员
#enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
for index, value in enumerate([1, 4, 5]):
    print(index, value)
# enumerate函数： 列表，字符串，元组
for index, value in enumerate("hello"):
    print(index, value)
for index, value in enumerate((1, 4, 8)):
    print(index, value)

# 扩展：加入想要获取遍历的是第几个键值对的下标，并且通过key获取value
my_dict = {"name": "李广", "age": 20, "sex": "男"}
for index, item in enumerate(my_dict.items()):
    # print(index, item[0], item[1])
    # 拆包
    key, value = item
    print(index, key, value)

#4.公共方法1:
# +	[1, 2] + [3, 4]	[1, 2, 3, 4]	合并	字符串、列表、元组
# *	['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	复制	字符串、列表、元组
# in	3 in (1, 2, 3)	True	元素是否存在	字符串、列表、元组、字典
# not in	4 not in (1, 2, 3)	True	元素是否不存在	字符串、列表、元组、字典
# 字符串拼接
result = "hello " + "world"
print(result)
# 合并
result = [1,2] + [3, 4]
print(result)
result = (3,5) + (9, 0)
print(result)
# 复制
result = "A" * 3
print(result)
result = [12, 34] * 2
print(result)
result = ("星星", "月亮") * 2
print(result)
# in 判断参数是否在指定对象里面
result = "a" in "abcd"
print(result)
result = "苹果" in ["苹果", "鸭梨"]
print(result)
result = "草莓" in ("苹果", "鸭梨")
print(result)
result = "age" in {"name": "孟军伟", "age": 22, "sex": "男"}
print(result)
result = "孟军伟" not in {"name": "孟军伟", "age": 22, "sex": "男"}.values()
print(result)

#5.公共方法2:
# len(item)	计算容器中元素个数
# max(item)	返回容器中元素最大值
# min(item)	返回容器中元素最小值
# del(item)	删除变量

# len: 字符串，列表，元组，字典，集合
count = len("hello")
print("字符串长度:", count)
count = len([2,4])
print("列表长度:", count)
count = len(("hello", "你好"))
print("元组长度:", count)
count = len({"name": "陈小飞", "age": 19})
print("字典长度:", count)
count = len({"哈哈", "呵呵"})
print("集合长度:", count)
# 元组，字符串，列表 max, min
result = max("1a")
print(result)
result = max(["1", "2", "abc"])
print(result)
result = min(["1", "2", "abc"])
print(result)
# del函数
my_list = ["张三", "李四", "冯七"]
del(my_list[1])
print(my_list)
# 删除字典中键值对
my_dict = {"name": "李广", "age": 20, "sex": "男"}
del(my_dict["age"])
print(my_dict)
# del函数还可以删除变量
a = "哈哈哈哈"
# 删除a的对象，把对象释放
del(a)
print(a)