"""
1.单例:可以多次创建对象,但是内存地址始终是第一次分配的内存地址,单例可以完成不同模块之间的数据共享
单例使用场景:购物车等
"""
class Singleton(object):
    #定义类属性保存创建对象的结果
    __singleton = None
    #是否初始化一次的标记
    __is_first = False

    def __new__(cls, *args, **kwargs):
        #判断类属性是否是None,非空表示要创建对象
        if not cls.__singleton:
            #保存创建对象
            cls.__singleton = object.__new__(cls)

        return cls.__singleton

    def __init__(self, name, age):
        #判断是否是第一次,不是第一次进行初始化,以后不再进行初始化
        if not self.__class__.__is_first:
            self.name = name
            self.age = age
            #初始化完成以后,设置成为已经初始化的状态
            self.__class__.__is_first = True

#创建多个对象测试内存地址
s1 = Singleton("张三", 25)
print(s1.name, s1.age)
s2 = Singleton("李四", 28)
print(s2.name, s2.age)
print(s1, s2)

"""
2.异常:在使用python解释器执行代码的是遇到错误，代码不能再继续往下执行，会在控制台显示错误提示，那么像这样错误就是异常
"""
# ValueError: invalid literal for int() with base 10: 'f'
# 接收数据不是一个合法的数字字符串类型,,本应该输入int类型,但是我们输入的时候输入的是字符串
# option = int(input("请出拳(0:剪刀 1:石头 2:布):"))
# print(option, type(option))

# NameError: name 'a' is not defined
# 变量名或者参数名没有定义
# a = 10
# del a
# print(a)

# ZeroDivisionError: division by zero
# 分母为0的错误
# result = 1 / 0
# print(result)

# FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
# 文件没有找到的错误
# open("test.txt", "r")

class Student(object):
    def __init__(self):
        self.name = "张三"
        self.__age = 30
        super(Student, self).__init__()

    # 私有方法
    def __show_money(self):
        print("100万")

stu =  Student()
# AttributeError: 'Student' object has no attribute '__age'
# 在执行对象里面没有找到对应的属性或者方法
# stu.__age
# stu.__show_money()


"""
3.捕获异常:try-except ,目的： 不能让程序崩溃，然后出现问题给用户进行良好提示，增加代码的稳健性
"""
# try:
#     option = int(input("请出拳(0:剪刀 1:石头 2:布):"))
# except ValueError:
#     print("请输入合法的数字")

# try:
#     a = 10
#     del a
#     print(a)
# except NameError:
#     print("哈哈，有异常啦")

# 查看异常信息
# try:
#     a = 10
#     del a
#     print(a)
# except NameError as e: # as e：表示获取异常对象
#     print("哈哈，有异常啦")
#     # 查看异常信息
#     print(e)

# 比如：以后不确定异常类型，可以统一使用Exception去捕获，因为多数异常类型都是继承Exception
# try:
#     result = 1 / 0
# except Exception as f:
#     print(f, type(f))


# 扩展： 使用多个exception关键字处理不同的异常信息
try:
    result = 1 / 1
    a = 10
    del a
    print(a)
# except可以单独处理某些自己关注的异常
except NameError as e:
    print(e)

except ZeroDivisionError as e:
    print(e)

except Exception as f:
    print(f, type(f))


# 没有异常会执行else
try:
    result = 1 / 1
    print(result)
except Exception as e:
    print(e)
else:
    print("哈哈，这次操作没有出现异常")

# 有没有异常都会执行:finally语句
try:
    result = 1 / 0
    print(result)
except NameError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    # 有异常会执行except捕获异常
    print(e)
else:
    # 没有异常会执行
    print("哈哈，这次操作没有出现异常")
# finally语句：必须放到异常捕获代码的最后
finally:
    # 有没有异常都执行
    print("我很任性，有没有异常都会执行")


# 了解： 使用一个except 可以捕获多个异常类型
try:
    result = 1 / 0
    print(result)
    print(num)
except (ZeroDivisionError, NameError) as e:
    print(e)

"""
4.异常的传递:如果当期代码块没有捕获异常，那么异常信息会往上抛出，如果外面都没有去捕获这个异常那么程序会崩溃，抛出这个异常
"""
try:
    try:
        result = 1 / 0

    finally:
        print("有没有异常都要执行")
except Exception as e:
    print(e, type(e))

def show_info1():
    a = 10
    del a
    print(a)

def show_info2():
    try:
        show_info1()
    except Exception as e:
        print(e, type(e))

def show_info3():
    show_info1()

show_info2()

# 扩展： 异常传递的应用场景，如果里面的代码出现异常抛出信息打印显示不方便，我们可以在最外层进行捕获
try:
    show_info3()
except Exception as e:
    print(e)


"""
5.抛出自定义异常
"""
# 自定义异常类
class CustomException(Exception):
    def __init__(self, current_len, min_len):
        self.current_len = current_len
        self.min_len = min_len
        # 调用父类的构造方法
        super(CustomException, self).__init__()


    def __str__(self):
        return "当前数据长度是%d,最小长度是%d" % (self.current_len, self.min_len)

# try:
#     print(num)
# except Exception as e:
#     print(e)

# # 模拟异常
password = input("请设置密码:")
try:
    if len(password) < 6:
        # 抛出异常
        raise CustomException(len(password), 6)
        # raise 不仅可以抛出自定义异常还可以抛出系统的异常
        # raise NameError("name 'num' is not defined")
        # raise StopIteration("停止迭代")
except Exception as e:
    print(e, type(e))

"""
6.异常处理中抛出异常:就是使用except捕获住异常，然后不对异常进行处理，
然后在抛出异常让外界进行处理这个异常
"""
try:
    try:
        result = 1 / 0
        print(result)
    except Exception as e:
        # 捕获异常
        # print(e)
        # 异常可以不进行处理可以向外进行抛出
        # raise e
        raise # 如果不指定异常对象，默认抛出当前异常
except Exception as e:
    print(e, type(e))


"""
7.模块:通俗理解一个.py文件就是一个模块，模块里面可以定义类，函数，变量，还可以理解成是一个工具箱
"""
# 定义类
class Student(object):
    def show(self):
        print("我是一个好学生")

# 定义函数
def show_student(student):
    student.show()

# 全局变量
num = 1

student = Student()
show_student(student)


"""
8.模块的导入
"""
# 方法以:导入第一个模块使用模块里面的功能代码
import first_module # 推荐大家使用这种方式进行导入，原因：不会出现代码覆盖的问题
# 只导入模块 访问方式 = 模块名.功能代码
person = first_module.Person("张三", 18)
person.run()

# 使用模块里面的功能函数
result = first_module.calc_num(1,2)
print(result)

print(first_module.num)

#方法二:通过模块导入指定功能代码
from first_module import Person
from first_module import calc_num
p = Person("张三", 18)
p.run()

result = calc_num(1, 2)
print(result)

# 注意点：使用from导入指定功能代码，如果在当前模块提供相同的代码，那么会把导入模块的代码覆盖

def calc_num(num1, num2):
    print("当前模块")
    return num1 + num2
result = calc_num(3, 2)
print(result)

#方法三:通过模块把模块里面的所有功能代码导入过来
from first_module import *
person = Person("尼古拉斯赵四", 45)
person.run()
result = calc_num(5, 4)
print(result)
print(num)

#扩展
# 既想使用当前模块的函数又想使用导入模块里面的函数那么可以使用import方式导入
# import first_module
#
# def calc_num(num1, num2):
#     print("当前模块")
#     return num1 + num2
#
# calc_num(1, 3)
#
# first_module.calc_num(4, 5)
# 可以给导入的模块起别名

# import first_module as first
#
# def calc_num(num1, num2):
#     print("当前模块")
#     return num1 + num2
#
# calc_num(1, 3)
#
# first.calc_num(4, 5)

# 注意点： 创建模块的时候不要使用和系统相同的名字
# import random
# # 随机数字的范围是0-2
# num = random.randint(0, 2)
# print(num)


# import sys
# # 查看模块导入的顺序
# # 提示: 默认在当前目录下查找，如果找到了就直接使用
# print(sys.path)


# from first_module import *
# result = calc_num(1, 2)
# print(result)
# # print(num)

import first_module

result = first_module.calc_num(2,3)
print(result)


"""
9.判断是否是主模块
"""
import second_module

# 调用模块里面的功能函数
result = second_module.sum_num(3, 5)
print("结果是:", result)

print(__name__)


"""
10.包:把不同模块(.py文件)放到文件夹里面进行管理就是一个包，但是要有一个前提是文件夹里面必须要有一个__init__.py的文件
提示： python3里面创建一个包会自动创建__init__.py文件，不需要我们自己手动创建
"""
#包的使用
# *** 导入包对应的模块
# import first_package.recv_msg
# import first_package.send_msg
#
# # 使用包对应模块里面的功能代码
# recv = first_package.recv_msg.Recv()
# recv.recv_data()
#
# send = first_package.send_msg.Send()
# send.send_data()
# 给导入的模块起别名
# import first_package.recv_msg as recv
# import first_package.send_msg as send
#
# recv.Recv().recv_data()
# send.Send().send_data()

# *** 通过包导入指定模块
# from first_package import recv_msg
# from first_package import send_msg
# recv_msg.Recv().recv_data()
# send_msg.Send().send_data()

# 通过包对应模块导入指定功能代码， 注意点：导入指定功能代码如果在当前模块定义相同的代码，那么会覆盖导入功能的代码
# from first_package.send_msg import Send
# from first_package.recv_msg import Recv
# from first_package.recv_msg import show
# Send().send_data()
# Recv().recv_data()
#
#
# def show():
#     print("哈哈，我是来捣乱的")
#
# show()

# *** 既想使用当前模块代码又想使用其他模块代码，可以使用以下方式去导入
# from first_package import recv_msg
# import first_package.recv_msg
# def show():
#     print("哈哈，我是来捣乱的")
#
# show()
# recv_msg.show()
# first_package.recv_msg.show()


# 导入包里面的所有模块,默认不会把包里面的所有模块进行导入。
# 想要全部导入需要自己在init文件里面进行配置
# from first_package import *
# recv_msg.Recv().recv_data()
# send_msg.Send().send_data()

# 直接导入包名的问题,默认不可以使用包里面的模块的，但是可以在init文件里面进行配置使用
# 想要使用需要在__init__.py里面进行配置，导入指定的模块
import first_package
first_package.recv_msg.Recv().recv_data()
first_package.send_msg.Send().send_data()









