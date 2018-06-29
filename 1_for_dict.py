# _*_ coding:utf-8 _*_

#第一,注释,中文支持问题,变量类型,标识符,关键字,输出,格式化输出,输入
# 1.python程序
print("hello world")

#2.注释:可以提高代码的可读性, _*_ coding:utf-8 _*_ 在python2里面指定中文的编码格式 ,多行注释可以做文档描述
#单行注释:  '#'单行注释
#多行注释: 使用三个单引号和三个双引号都可以做注释

#3.两数相加的功能函数
def sum(num1, num2):
    return num1 + num2
#调用两数相加的功能函数并用一个变量保存
result = sum(3,5)
print(result)

#4.# _*_ coding:utf-8 _*_  #  ’# 添加中文编码格式方式2 python推荐使用的‘， 表示可以兼容python2和python3的代码
# coding=utf-8'  # 添加中文编码格式方式1
# 测试python2和python3中文支持问题
def show(name, age, sex):
    print(name, age, sex)
show("宋雨希", 25, "女")

#5.变量:通俗理解可以认为是存储程序中数据的容器 定义变量的格式     变量名 = 数据
#定义了变量  名字是a 存储的数据是10
"""
变量的类型:
(1)Numbers(数字)------>int(有符号整形)
            ------->long(长整形)
            ------->float(浮点型)
            ------->complex(复数类型,基本不用)
(2)布尔类型 (True和False)
(3)String(字符串)
(4)List(列表)
(5)Tuple(元祖)
(6)Dictionary(字典)
总结:可变类型有(字典,列表,集合)   不可变类型有(数字类型,字符串,元祖)
"""
a = 10
#定义了变量,名字叫做b,存储的数据是:hello world 字符串
b = "hello world"
#通过type可以查看变量的类型, 不要使用内置类型的变量名
print(type(a))   #int类型
print(type(b))   #str类型

#6.标识符: 变量名标识符是有字母,数字,下划线组成的,并且数字不能开头
#命名规则:驼峰命名法和下划线命名法
#驼峰命名法:小驼峰和大驼峰
#小驼峰是第一个单词首字母小写,其他单词首字母大写
#大驼峰是每个单词首字母都大写
#推荐使用下划线命名法,所有单词都小写,单词之间使用下划线进行分割

#7.import  导入模块关键字
import keyword
#关键字不能作为变量名
#获取关键字列表
result = keyword.kwlist
print(result)

#8. 输出内容使用print
print("hello  world")
score = 100
print(score)
#输出多个值
name = "宋雨希"
age = 15
#多个参数输出的时候,参数之间用使用逗号和空格分割
print(name, age)
#sep表示设置参数之间分割的标识符
print(name, age, sep=":")
#转到定义快捷键 ctr + b
#end 表示输出打印的结尾标识符,把结尾表示设置为空字符串不在进行换行
print("hello world", end="")
print(score, end="")

#9.格式化输出:
a = 10
#%d:表示格式化占位符,表示整数进行格式化
print("我今年的年龄是%d" % age)
#格式化多个参数
name = "宋雨希"
age = 28
print("我的名字是%s, 年龄是%d" % (name, age))
#%f:格式化占位符会对浮点数进行四舍五入,默认保留6位小数
pi = 3.1415926
print("%f" % pi)
#保留两位小数
print("%.2f" % pi)
#需求只是一个print ,但是输出的内容由换行
print("哈哈,\n今年我已经\n18岁了,\n太开心了,\n可以去网吧玩游戏了")
# demo
name = input("请输入您的姓名:")
tel = input("请输入您的电话:")
address = input("请输入您的地址:")
company = input("请输入您的公司:")
print("="*30)
print("姓名%s" % name)
print("电话:%s" % tel)
print("公司地址:%s" % address)
print("公司名称:%s" % company)
print("="*30)

#10,输入
"""
1.输入:程序等待用户数据数据,程序接受到用户输入的数据以后可以继续执行,否则一直等待用户输入数据
2.python2里面的raw_input 和python3里面的input功能一样,返回的数据类型是字符串

"""
#input ()接受表达式输入,并把表达式结果赋值给等号左边的变量
# content = raw_input("请输入您的信息")
# print(content, type(content))
# content = input("请输入您的信息")
# print(content, type(content))

"""
python3接受用户输入的数据使用input函数
字符串参数表示提示用户输入的信息内容

"""

#第二,算数,赋值,复合赋值运算符,数据类型转换,if判断,比较和逻辑运算符,if嵌套,while循环和嵌套
#1.算数运算符
# +	加	两个对象相加 a + b 输出结果 30
# -	减	得到负数或是一个数减去另一个数 a - b 输出结果 -10
# *	乘	两个数相乘或是返回一个被重复若干次的字符串 a * b 输出结果 200
# /	除	b / a 输出结果 2
# //	取整除	返回商的整数部分 9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
# %	取余	返回除法的余数 b % a 输出结果 0
# **	指数	a**b 为10的20次方， 输出结果 100000000000000000000

"""
注意：混合运算时，优先级顺序为： ** 高于 * / % // 高于 + - ，为了避免歧义，建议使用 () 来处理运算符优先级。

并且，不同类型的数字在进行混合运算时，整数将会转换成浮点数进行运算。
"""
num1 = 2
num2 = 3
#+
result = num1 + num2
print(result)
#-
result = num1 - num2
print(result)
# *
result = num1 * num2
print(result)
# /  提示： 数据相除以后类型编程浮点类型
result = num1 / num2
print(result, type(result))
# //  求商
result = num1 // num2
print(result)
# % 求余数
result = num1 % num2
print(result)
# 求次方
result = num1 ** num2
print(result)
# 计算优先级
result = (num1 + num2) * 3
print(result)
#需求:计算商品的页数
#1. 获取商品总数
num = int(input("请输入商品总数:"))
#2. 获取每页显示的数量
numEachPage = int(input("请输入每页的商品数量:"))
#3. 计算并显示结果
pageNum = num // numEachPage
pageNum2 = num % numEachPage
#判断是否能整除,否则意味着 需要多余的一页来显示商品
if pageNum2 == 0:
    print("商品的页数为:%d"%pageNum)
if pageNum2 != 0:
    print("商品页数为:%d"%(pageNum+1))


#2.赋值运算符 "="
num = 100
# 给多个变量赋值
num1, num2 = 2, 4
print(num1, num2)


#3.复合赋值运算符
# +=	加法赋值运算符	c += a 等效于 c = c + a
# -=	减法赋值运算符	c -= a 等效于 c = c - a
# *=	乘法赋值运算符	c *= a 等效于 c = c * a
# /=	除法赋值运算符	c /= a 等效于 c = c / a
# %=	取模赋值运算符	c %= a 等效于 c = c % a
# **=	幂赋值运算符	c **= a 等效于 c = c ** a
# //=	取整除赋值运算符	c //= a 等效于 c = c // a
num1 = 3
num2 = 5
# +=
# num1 += num2  # 等价于num1 = num1 + num2
# print(num1)

# -=
# num1 -= num2 # 等价于num1 = num1 - num2
# print(num1)

# *=
# num1 *= num2 # 等价于num1 = num1 * num2
# print(num1)

# %=
# num1 %= num2  # 等价于num1 = num1 % num2
# print(num1)

# **=
# num1 **= num2 # 等价于num1 = num1 ** num2
# print(num1)

# //=
num1 //= num2  # num1 = num1 // num2
print(num1)


#4.数据类型转换
# int(x [,base ])	将x转换为一个整数
# float(x )	将x转换为一个浮点数
# complex(real [,imag ])	创建一个复数，real为实部，imag为虚部
# str(x )	将对象 x 转换为字符串
# repr(x )	将对象 x 转换为表达式字符串
# eval(str )	用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(s )	将序列 s 转换为一个元组
# list(s )	将序列 s 转换为一个列表
# chr(x )	将一个整数转换为一个Unicode字符
# ord(x )	将一个字符转换为它的ASCII整数值
# hex(x )	将一个整数转换为一个十六进制字符串
# oct(x )	将一个整数转换为一个八进制字符串
# bin(x )	将一个整数转换为一个二进制字符串

# my_str = "123"
# result = int(my_str)
# print(result, type(result))

# # 提示: 浮点数字符串不能直接转成int类型，可以转成float类型，然后在转成int类型
# my_str = "3.14"
# result = float(my_str)
# print(result, type(result))
# # 代码执行到此，result变量是float类型，现在是把float类型转成int类型
# value = int(result)
# print(value, type(value))

# value = 3.5
# # 提示： int类型转换的是没有四舍五入，%.2f格式符号会有四舍五入
# result = int(value)
# print(result)

# result1 = complex(4, 3)
# print(result1, type(result1))
# result2 = complex(2, -1)
# print(result1, type(result1))
# result = result1 + result2
# print(result)

# 数字可以转成字符串
# num = 123.5
# result = str(num)
# print(result, type(result))

# result = str("xixi")
# print(result, type(result))
# 提示：如果是字符串那么会把字符串作为一个整体在放入到一个字符串中，最终类型还是字符串类型
# result = repr("xixi")
# print(result, type(result))

# 将一个字符转换为它的ASCII整数值
# result = ord("a")
# print(result, type(result))

# 把整数转成16进制
# 0x表示16进制数据
# %x：转成十六进制的格式化符号
# result = hex(10)
# print(result, type(result))

# 0o表示8进制数据
# result = oct(10)
# print(result, type(result))

# 0b表示二进制数据
result = bin(10)
print(result, type(result))


#5.if判断  格式
#if 判断的条件
    #条件成立可以执行的if语句
age = int(input("请输入您的年龄"))
if age>= 18:
    print("您已经成年了,可以去网吧上网了")
#需求:根据湿度判断天气
shiDu = int(input("请输入当前空气的湿度:(用数字表示)"))
if shiDu < 30:
    print("干燥")
if shiDu > 60:
    print("潮湿")
#需求:简单计算器
num1 = int(input("请输入第一个数字:"))
num2 = int(input("请输入第二个数字:"))
op = input("请输入要进行操作的方式(加+ 减- 乘* 除/ )")
#根据计算方式输出相应结果
if op == "+":
    print("%d+%d=%d" % (num1, num2, num1 + num2))
if op == "-":
    print("%d-%d=%d" % (num1, num2, num1 - num2))
if op == "*":
    print("%d*%d=%d" % (num1, num2, num1 * num2))
if op=="/":
    print("%d/%d=%d"%(num1, num2, num1/num2))



#6.比较运算符
# ==	检查两个操作数的值是否相等，如果是则条件变为真。	如a=3,b=3，则（a == b) 为 True
# !=	检查两个操作数的值是否相等，如果值不相等，则条件变为真。	如a=1,b=3，则(a != b) 为 True
# >	检查左操作数的值是否大于右操作数的值，如果是，则条件成立。	如a=7,b=3，则(a > b) 为 True
# <	检查左操作数的值是否小于右操作数的值，如果是，则条件成立。	如a=7,b=3，则(a < b) 为 False
# >=	检查左操作数的值是否大于或等于右操作数的值，如果是，则条件成立。	如a=3,b=3，则(a >= b) 为 True
# <=	检查左操作数的值是否小于或等于右操作数的值，如果是，则条件成立。	如a=3,b=3，则(a <= b) 为 True
num1 = 1
num2 = 10

# 总结:使用比较运算符返回的结果是bool， bool类型只有两个值True和False
# 比较运算符一般都会结合if判断使用，True表示条件成立，Flase表示条件不成立
# result = (num1 == num2)
# print(result, type(result))

# result = (num1 != num2)
# print(result, type(result))

# result = num1 > num2
# print(result, type(result))

# result = num1 < num2
# print(result, type(result))

# result = num1 >= num2
# print(result)

# result = num1 <= num2
# print(result)


#7.逻辑运算符
# and	x and y	布尔"与"：如果 x 为 False，x and y 返回 False，否则它返回 y 的值。	True and False， 返回 False。
# or	x or y	布尔"或"：如果 x 是 True，它返回 True，否则它返回 y 的值。	False or True， 返回 True。
# not	not x	布尔"非"：如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not True 返回 False, not False 返回 True

# name = input("请输入您的姓名:")
# age = int(input("请输入您的年龄:"))

# and: 左右两边的条件都成立if语句才执行
# if name == "小明" and age == 18:
#     print("姓名:%s 年龄:%d" % (name, age))

# or： 左右两边至少有一个条件成立if语句就会执行
# if name == "小明" or age > 18:
#     print("姓名:%s 年龄:%d" % (name, age))

result = (3 == 3)
print(result)
# not:表示取反，True取反是False， Flase取反是True
if not result:
    print("条件成立")

#8.if和else使用
"""
 if 条件:
        满足条件时要做的事情1
        满足条件时要做的事情2
        满足条件时要做的事情3
        ...(省略)...
    else:
        不满足条件时要做的事情1
        不满足条件时要做的事情2
        不满足条件时要做的事情3
        ...(省略)...
"""
# 接收用户输入的年龄
age = int(input("请输入您的年龄:"))
# if条件成立执行if语句，如果条件不成立那么执行else语句
if age >= 18:
    print("哥成年了，可以进入网吧玩耍")
else:
    print("不好意思，再忍几年")
#需求:判断是不是白富美
#1. 获取她的肤色
color = input("请输入她的肤色(白/黄/黑):")
#2. 获取她的资产
money = int(input("请输入她的资产信息:"))
#3. 获取她的颜值
beautiful = input("请输入她的颜值(0:美  1:普通):")
#4. 判断是否符合白富美的标准
if color=="白" and money>=1000000  and beautiful=="0":
    print("白富美.....一定要娶她")
else:
    print("不是白富美.....当做普通朋友")


#9.elif使用
"""
 if xxx1:
        事情1
    elif xxx2:
        事情2
    elif xxx3:
        事情3
当xxx1满足时，执行事情1，然后整个if结束
当xxx1不满足时，那么判断xxx2，如果xxx2满足，则执行事情2，然后整个if结束
当xxx1不满足时，xxx2也不满足，如果xxx3满足，则执行事情3，然后整个if结束


if 性别为男性:
       输出男性的体重
       ...
   elif 性别为女性:
       输出女性的体重
       ...
   else:
       第三种性别的体重

当 “性别为男性” 满足时，执行 “输出男性的体重”的相关代码
当 “性别为男性” 不满足时，如果 “性别为女性”满足，则执行 “输出女性的体重”的相关代码
当 “性别为男性” 不满足，“性别为女性”也不满足，那么久默认执行else后面的代码，即 “第三种性别的体重”相关代码

elif必须和if一起使用，否则出错
else 一般用在最后，即所有条件都不满足时使用
"""
# 接收用户的分数
score = int(input("请输入您的分数"))

# if elif 判断如果某个条件成立，后面的条件判断就不执行了，判断语句执行结束
# if elif else 最终只执行一个条件语句
if score >= 90 and score <= 100:
    print("优秀")
elif score >= 80 and score < 90:
    print("良好")
elif score >= 70 and score < 80:
    print("一般")
elif score >= 60 and score < 70:
    print("差")
else:
    print("不及格")
#需求:简单计算器
#1. 获取一个数
num1 = int(input("请输入第1个数:"))
#2. 获取第二个数
num2 = int(input("请输入第2个数:"))
#3. 获取计算方式
op = input("请输入要进行的操作(加+ 减- 乘* 除/):")
#4. 根据计算方式输出相应的结果
if op=="+":
    print("%d+%d=%d"%(num1, num2, num1+num2))
elif op=="-":
    print("%d-%d=%d"%(num1, num2, num1-num2))
elif op=="*":
    print("%d*%d=%d"%(num1, num2, num1*num2))
elif op=="/":
    print("%d/%d=%d"%(num1, num2, num1/num2))
else:
    print("您输入的操作有误,请重新运行并且输入")
#需求:显示日期
#1. 获取一个数字
num = int(input("请输入一个数字(1-7):"))
#2. 使用if-elif-else来进行判断,并显示对应的信息
if num==1:
    print("周一")
elif num==2:
    print("周二")
elif num==3:
    print("周三")
elif num==4:
    print("周四")
elif num==5:
    print("周五")
elif num==6:
    print("周六")
elif num==7:
    print("周日")
else:
    print("输入的数据有误,请重新输入")
# 扩展：
# 判断名字是否是小明，如果是小明打印小明信息  判断年龄是否是18如果成立打印年龄
name = "小明"
age = 18
# 如果每个条件都判断可以使用if语句单独进行判断
if name == "小明":
    print(name)

if age == 18:
    print(age)
#扩展if  not使用
#1. 获取她的肤色
color = input("请输入她的肤色(白/黄/黑):")
#2. 获取她的资产
money = int(input("请输入她的资产信息:"))
#3. 获取她的颜值
beautiful = input("请输入她的颜值(0:美  1:普通):")
#4. 判断是否符合白富美的标准
'''
if color!="白" and money<1000000  and beautiful!="0":
    print("矮矬穷.....一定要娶她")
else:
    print("不是矮矬穷.....当做普通朋友")
'''
#下面的这一行代码,仅仅是对白富美这个结果 取反
#if not (color=="白" and money>=1000000 and beautiful=="0"):
#下面的代码,是对每一个条件都进行取反
if (not color=="白" )  and ( not money>=1000000)  and (not beautiful=="0"):
    print("矮矬穷.....一定要娶她")
else:
    print("不是矮矬穷.....当做普通朋友")


#10.if嵌套
"""
 if 条件1:

        满足条件1 做的事情1
        满足条件1 做的事情2

        if 条件2:
            满足条件2 做的事情1
            满足条件2 做的事情2

外层的if判断，也可以是if-else
内层的if判断，也可以是if-else
根据实际开发的情况，进行选择
"""
# 模拟男生找女朋友的例子
sex = input("请输入您的性别:")
if sex == "女":
    print("您是非常漂亮的女生")

    age = int(input("性别复合了,麻烦您再输入您的年龄:"))

    if age >= 20 and age <= 30:
        print("您的年龄也复合我的要求")

        height = int(input("性别和年龄您都复合了,最后请您输入您的身高:"))
        if height >= 160 and height <= 180:
            print("您太完美了,简直就是我的女神")
        else:
            print("不好意思您的身高不太复合")
    else:
        print("您的念梁不太复合")

else:
    print("不好意思我想找的是一个女生")
#需求:购买火车票上车
ticket = 0 #1 表示有火车票  0表示没有火车票
knifeLength = 20 #cm
#先判断是否有车票
if ticket == 1:
    print("顺利的通过了检票口,可以进入到下一关的安检了....")
    #判断刀子的长度是否符合要求
    if knifeLength <= 10:
        print("安检通过,可以进入到候车室等待 开往 家乡的列车了,,好激动....")
    else:
        print("安检没有通过,等待公安的处理....")
else:
    print("小伙子,先去买车票啊...没票是不能上车的.....")
#需求:登陆系统简单版
#1. 获取用户名
name = input("请输入用户名:")
#2. 获取密码
passwd = input("请输入密码:")
#3.判断用户名和密码是否正确
if name == "dongge" and passwd == '123456':

    print("用户名和密码验证成功,请进行二次验证")

    #4. 在第3步成立的基础上,进行二次验证
    print("已经成功的向您的手机发送了验证码")

    yanzhengma = input("请收入您手机上的验证码:")

    if yanzhengma == '112233':
        print("恭喜你 登陆成功!")
    else:
        print("验证码错误,请重新输入")

else:
    print("用户名或者密码错误")



#11.猜拳游戏
import random

# 接收用户输入的数据
player = int(input("请出拳 剪刀(0) 石头(1) 布(2):"))

# 点击随机出拳，产生随机数字
computer = random.randint(0, 2)  # 0-2之间随机产生一个整型数字

if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("您赢了，电脑输了")
elif player == computer:
    print("平局，再来一次")
else:
    print("您输了，电脑赢了")


#12.while循环的使用
"""
 while 条件:
        条件满足时，做的事情1
        条件满足时，做的事情2
        条件满足时，做的事情3
        ...(省略)...
"""
count = 1
while count <= 3:
    print("好好学习 天天向上")
    count += 1
#需求:循环的时候打印当前循环的次数,上限是5
current_count = 1
while current_count <= 5:
    print("当前循环的次数是:", current_count)
    current_count += 1
#需求:显示100-1之间的数字
num=100
while num > 0 :
    print("%d"%num)
    num -= 1


#13.  1-100的累计和
#获取1到100的数字进行相加,得到相加后的结果
#从1开始循环
num = 1
#1-100数字相加保存的结果变量
result = 0
while num <= 100:
    #计算每个数据相加的结果
    result += num
    # 获取1-100的每一个数字
    num += 1
print(num)
print(result)

#14需求:计算1-100之间的偶数和
num = 1
result = 0
while num <= 100:
    if num % 2 == 0:
        result += num
    num += 1
print(result)


#15.while循环嵌套,在while循环里面还由一耳光while循环
"""
while 条件1:

        条件1满足时，做的事情1
        条件1满足时，做的事情2
        条件1满足时，做的事情3
        ...(省略)...

        while 条件2:
            条件2满足时，做的事情1
            条件2满足时，做的事情2
            条件2满足时，做的事情3
            ...(省略)...
"""
#while嵌套的格式
i = 0
while i < 5 :
    print("i = %d" % i)
    j = 0
    while j < 3:
        print("j=%d" % j)
        j += 1
    i += 1
#需求:每输出一个数字,打印两遍今天很开心
count = 1
while count <= 3:
    print(count)
    inner_count = 1
    while inner_count <= 2:
        print("今天很开心呢")
        inner_count += 1
    count += 1
#需求:打印矩形
i = 0
while i < 8:
    j = 0
    while j < 6:
        #end= 没有end的时候,打印完数据后默认换行
        #end= 加上则表示打印完数据后不会换行此时,光标还在当前行中
        print("*", end="")
        j += 1
    #用来换行,否则左右的*都会在一行中显示
    print("")
    i += 1

#16.打印三角形
row = 1
while row <= 9:
    print(row)

    col = 1
    while col<= row:
        print("*", end="")
        col += 1

    print("")
    row += 1
#需求:打印九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%d\t"%(j,i,j*i), end="")
        j += 1
    print("")
    i += 1
#扩展break和continue在循环中的作用
i = 0
print("while start==========")
while i<5:
    i+=1
    print("----------")
    if i==3:
        #break #break 只要被执行到了,那么就相当于这while循环结束了
        continue# continue只要被执行到了,那就相当于 这次循环中 后面的代码不会被执行
                #而是执行下一次的循环
    print("i=%d"%i)
print("while stop========")
#需求:登陆的高级版
import time
loginNums = 0
while loginNums<5:
    #1. 获取用户名
    name = input("请输入用户名:")
    #2. 获取密码
    passwd = input("请输入密码:")
    #3. 判断用户名和密码是否正确
    if name == "dongge" and  passwd == '123456':
        print("用户名和密码验证成功,请进行二次验证")
        #4. 在第3步成立的基础上,进行二次验证
        print("已经成功的向您的手机发送了验证码")
        yanzhengma = input("请收入您手机上的验证码:")
        if yanzhengma == '112233':
            print("恭喜%s 登陆成功!"%name)
            break
        else:
            print("验证码错误,请重新输入")
    else:
        print("用户名或者密码错误")
        i = 5
        while i>0:
            print("请等待....%d"%i)
            time.sleep(0.5)
            i-=1
    loginNums+=1





my_dict = {"name": "李广", "age": 20, "sex": "男"}

# 默认遍历字典获取的每一个key
for key in my_dict:
    value = my_dict[key]
    print(key, value)




print("------------------------------------------")
# 遍历所有的value值
for value in my_dict.values():
    print(value)

print("------------------------------------------")

# 遍历所有的key值
for key in my_dict.keys():
    print(key)

print("------------------------------------------")

# 遍历每项数据的key和value值
for item in my_dict.items():
    print(item[0],item[1])

print("------------------------------------------")

# 拆包获取元祖里面的数据
for key, value in my_dict.items():
    print(key, value)
print("------------------------------------------")

# enumerate函数获取对象中成员下表和成员
for index, value in enumerate("hello"):
    print(index, value)

print("------------------------------------------")

for index, value in enumerate((1,4,5,8,9)):
    print(index, value)

print("------------------------------------------")

# 获取遍历的是第几个键值对的下表,并且通过key获取value

for index, item in enumerate(my_dict.items()):
    key, value = item
    print(index, key, value)
