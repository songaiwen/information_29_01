"""
1.  # 可变类型: 在原有数据的基础上可以对数据进行修改(添加或者删除或者修改)，修改后内存地址不变
    # 可变类型有： 字典，列表，集合
    # 不可变类型：不能再原有数据的基础上对数据进行修改
    # 不可变类型： 数字，字符串，元组

"""
# 不可变数据类型： 字符串，元组， 数字
#数字
my_num = 1
print(id(my_num))
# my_num[0] = 2
# 注意点： 这个不是修改数据，是修改的变量对应的内存地址
my_num = 2
print(id(my_num))
#字符串
my_str = "hello"
print(id(my_str))
# 测试修改数据,错误的示范
# my_str[0] = "H"
# print(id(my_str))
#元祖
my_tuple = (3, 6)
print(id(my_tuple))
# 测试修改数据,错误的示范
# my_tuple[0] = 1
# print(id(my_tuple))

#可变类型有： 字典，列表，集合
#字典
my_dict = {"name": "zs", "age":20}
# id查看变量保存的内存地址
print(id(my_dict))
#修改字典
my_dict["name"] = "张三"
print(id(my_dict))

#列表
my_list = [1, 3, 5]
print(id(my_list))
#修改列表
my_list[0] = 6
print(id(my_list))

#集合
my_set = {3, 45 ,6}
print(id(my_set))
# 修改集合
my_set.add(9)
print(id(my_set))

"""
2.函数的参数传递是引用的传递,在python里面所有的传递都是引用传递,也可以说是内存地址的传递
"""
def show_info(info):
    #查看参数的内存地址
    print(id(info))
    #通过计算查看内存地址的变化
    # info += info
    # 赋值操作内存地址会发生变化，因为先计算等号右边结果，把结果对应的内存地址给等会左边变量
    info = info + info
    print(id(info))
    # 以上两种操作对应不可变类型来说，info保存的内存地址都发生了变化
    # 提示： 对应可变类型来说 += 操作内存地址不变，因为在自己数据的基础上继续的修改，
    # 而info = info + info 是先计算相加后的结果把结果所对应的内存地址给info变量， 所以内存地址发生变化

my_list = [1, 2]
print(id(my_list),my_list)

show_info(my_list)

"""
3.函数的使用注意点
"""
# 定义第一个函数
def show_num():
    num = 10
    print(num)
show_num()
# 定义第二个参数
def show_num(num):
    print(num)
show_num(20)
# 调用第一个函数
# 在python里面函数名如果相同，会把之前定义的函数覆盖，以前的函数不能在最后使用
# 建议： 如果没有特殊的需要，函数不要相同
show_num(50)

"""
4.递归函数:在函数里面调用当前函数本身就是递归函数
"""
import sys
# 3! = 3 * 2 * 1

# result = 1
# for value in range(3, 0, -1):
#     result *= value
#
# print(result)

# 3! = 3 * 2!
# 2! = 2 * 1!
# 1！ = 1

# # 计算3阶乘函数
# def calc_num(num):
#     return num * calc_num(2)

# # 计算2阶乘函数
# def calc_num(num):
#     return num * calc_num(1)

# # 计算1阶乘函数
# def calc_num(num):
#     if num == 1:
#         return 1

# 根据传入过来的数字计算对应的阶乘函数
# def calc_num(num):
#     if num == 1:
#         return 1
#     else:
#         return num * calc_num(num-1)
# 扩展：
# 递归调用有上限控制
# 获取默认的递归次数
count = sys.getrecursionlimit()
print(count)
# 设置递归次数
sys.setrecursionlimit(1100)
count = sys.getrecursionlimit()
print(count)

# result = calc_num(1000)
# print(result)

"""
5.匿名函数:不适用def关键字定义的函数就是匿名函数, 可以完成类似比较简单的功能函数,简化普通函数的作用
"""
#一个普通函数,计算两个数的和
def sum(num1, num2):
    return num1 + num2

result = sum(1, 2)
print(result)

# lambda表达式的格式
#lambda [arg1 [,arg2,.....argn]]:expression
# num1, num2 匿名函数的参数
# num + num: 冒号后面写表达式结果
func = lambda num1, num2: num1 + num2
result = func(1,2)
print(result)
# Lambda函数能接收任何数量的参数但只能返回一个表达式的值
# 匿名函数不能直接调用print，因为lambda需要一个表达式
#扩展:匿名函数还可以结合if判断使用
func = lambda x: True if x % 2 == 0 else False
#执行函数
result = func(1)
print(result)

#扩展:匿名函数还可以作为其他函数的参数,当然def函数也是可以作为其他函数的参数的
def show_info(function):
    print(function)
    num1 = 1
    num2 = 2
    #执行传入过来的函数
    result = function(1,2)
    return result

#定义匿名函数,作为函数参数
func = lambda num1, num2: num1 + num2
result = show_info(func)
print(result)

#定义show_info所需要的函数类型
def show_info(num1, num2):
    print(num1, num2)
#函数名就是一个对象,我们还可以使用变量保存函数在内存中的地址
a = show_info
print(a)
#需求:匿名函数的应用场景:
my_list = [{"name":"songyuxi", "age":28}, {"name":"songjiaying", "age":25}]
#根据key对应的value值进行字典的排序
#x:表示排序的时候遍历的每一个字典,x["age"]:通过key获取value值进行比较，完成排序
# my_list.sort(key=lambda x:x["age"], reverse=True)
my_list.sort(key=lambda x:x["name"])

print(my_list)

"""
6.给程序传参
"""
import sys
#获取给程序传入的参数
params_list = sys.argv
#想要获取参数列表后面的值,需要判断参数列表的长度是否大于1,如果大于1需要至少两个
if len(params_list) > 1:
    #从1下标开始获取到最后一个下标
    result = params_list[1:]
    print(result)
print(params_list, type(params_list))


"""
11.列表推倒式也叫列表生成式, 起始就是使用for循环快速生成创建一个列表
"""
#生成0-4的5个数字的列表
my_list1 = [value for value in range(5)]
print(my_list1, type(my_list1))
#生成1-10的列表
my_list2 = [value for value in range(1, 11)]
print(my_list2)
#生成1-11步长为2的列表
my_list3 = [value for value in range(1, 11, 2)]
print(my_list3)

#列表生成式也可以添加if判断
my_list4 = [value for value in range(1, 11) if value % 2 == 0]
print(my_list4)

#使用列表生成式创建元祖列表(二维)
my_list5 = [(value1, value2) for value1 in range(3) for value2 in range(3)]
print(my_list5)
#三维数组
my_list6 = [(value1, value2, value3) for value1 in range(3) for value2 in range(3) for value3 in range(3)]
print(my_list6)

"""
12.集合列表元组等类型的转换
"""
# 1.列表转集合
my_set = set([1,3,3,4,6])
# 集合可以对列表，元组数据进行去重
print(my_set, type(my_set))
#2.元组转集合
my_set = set((1,3,3,3,5))
print(my_set, type(my_set))
#3.集合转列表
my_list = list({3,5,6})
print(my_list, type(my_list))
#4.元祖转列表
my_list = list((1,4,7))
print(my_list, type(my_list))
#5.集合转元组
my_tuple = tuple({1,2,3,4})
print(my_tuple, type(my_tuple))
#6.列表转元组
my_tuple = tuple([1,2,5,7,9])
print(my_tuple, type(my_tuple))
#总结:元祖,列表,集合三者可以互相转换

"""
13.set集合的使用
"""
#set集合:数据的集合,无序, 集合里面没有重复数据,可以添加,删除,但是不能根据下标修改或者根据下标获取元素
#集合是可变类型
#注意点:下面的方式表示的是字典,不是set集合类型
my_set = {}
print(type(my_set))
#需要通过set类创建set对象就是一个空的集合
my_set = set()
#查看变量保存的内存地址
print(id(my_set))
print(my_set, type(my_set))
#添加元素
my_set.add(1)
print(my_set)
print(id(my_set))
# 扩展： 删除元素有两种方式
# 方式1
# my_set.remove(2)  # 注意如果删除的元素没有集合里面那么会崩溃
# print(my_set)
# 方式2
my_set.discard(1)  # 如果元素在集合里面那么删除元素，如果不在就不删除不会崩溃
print(my_set)

# 测试： 根据下标修改集合的元素
# 错误的写法
# my_set[0] = "你好"
# print(my_set)

# 错误的写法，不能根据下标获取对应的元素
# result = my_set[0]
# print(result)

# 遍历集合
for value in my_set:
    print(value)

# 扩展:
my_set1 = {1, 3, 5}
my_set2 = {3, 5, 6}
# 交集 &
result = my_set1 & my_set2
print(result)
# 并集
result = my_set1 | my_set2
print(result)

# 差集
result = my_set1 - my_set2
print(result)

# 等差差集
result = my_set1 ^ my_set2
print(result)

















































