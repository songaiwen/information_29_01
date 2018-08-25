"""
1.常见时间复杂度
    执行次数函数举例	         阶	                          非正式术语
    12	                     O(1)	                      常数阶
    2n+3	                 O(n)	                       线性阶
    3n2+2n+1	             O(n2)	                       平方阶
    5log2n+20	             O(logn)	                   对数阶
    2n+3nlog2n+19	         O(nlogn)	                   nlogn阶
    6n3+2n2+3n+4	         O(n3)	                       立方阶
    2n	                     O(2n)	                       指数阶

注意，经常将log2n（以2为底的对数）简写成logn
时间复杂度之间的关系:
O(1) < O(logn) < O(n) < O(nlogn) < O(n2) < O(n3) < O(2n) < O(n!) < O(nn)
"""

#2.timeit模块可以用来测试一小段python代码的执行速度
"""
class timeit.Timer(stmt='pass', setup='pass', timer=<timer function>)
Timer是测量小段代码执行速度的类。

stmt参数是要测试的代码语句（statment）；

setup参数是运行代码时需要的设置；

timer参数是一个定时器函数，与平台有关。

timeit.Timer.timeit(number=1000000)
Timer类中测试语句执行速度的对象方法。number参数是测试代码时的测试次数，默认为1000000次。
方法返回执行代码的耗时，一个float类型的秒数。
"""
import timeit
from timeit import Timer
# li1 = [1, 2]
#
# li2 = [23,5]
#
# li = li1+li2
#
# li = [i for i in range(10000)]
#
# li = list(range(10000))

#用五种方式,得到包含一千个元素的列表
#数据结构
def t1():
    li = []
    for i in range(1000):
        li.append(i)

def t2():
    li = []
    for i in range(1000):
        # li = li + [i]
        li += [i]

def t3():
    li = [i for i in range(1000)]

def t4():
    li = list(range(1000))

def t5():
    li = []
    for i in range(1000):
        li.extend([i])

timer1 = Timer("t1()", "from __main__ import t1")
print("append:", timer1.timeit(1000))

timer2 = Timer("t2()", "from __main__ import t2")
print("+:", timer2.timeit(1000))

timer3 = Timer("t3()", "from __main__ import t3")
print("[i for i in range]:", timer3.timeit(1000))

timer4 = Timer("t4()", "from __main__ import t4")
print("list(range()):", timer4.timeit(1000))

timer5 = Timer("t5()", "from __main__ import t5")
print("extend:", timer5.timeit(1000))


def t6():
    li = []
    for i in range(10000):
        li.append(i)

def t7():
    li = []
    for i in range(10000):
        li.insert(0, i)


timer6 = Timer("t6()", "from __main__ import t6")
print("append", timer6.timeit(1000))    #3.1731402490040637

timer7 = Timer("t7()", "from __main__ import t7")
print("insert(0)", timer7.timeit(1000))  #53.47018265999941

# 从结果可以看出，append从尾端添加元素效率远远高于insert从顶端添加元素

































