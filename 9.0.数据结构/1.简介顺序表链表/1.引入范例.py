"""
1.算法的概念理解:算法是计算机处理信息的本质,因为计算机程序本质是一个算法来告诉计算机确切的步骤
来执行一个指定的任务,一般的,当算法在处理信息时,会从输入设备或数据的存储地址读取数据, 把结果
写入输出设备或某个存储地址供以后调用

2.算法是独立存在的一种解决问题的方法和思想

3.五个特征
    输入 : 算法具有0个或多个输入
    输出 : 算法至少有1个或多个输出
    有穷性 : 算法在有限的步骤之后会自动结束而不会无限循环，并且每一个步骤可以在可接受的时间内完成
    确定性 ：算法中的每一步都有确定的含义，不会出现二义性
    可行性 ：算法的每一步都是可行的，也就是说每一步都能够执行有限的次数完成

"""


"""
如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?

"""
#第一种思想
#时间复杂度：
#T(n) = O(n*n*n*10) =O(n^3)

import time
# #枚举法
# start_time = time.time()
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             #判断条件三个数字和为1000 a方加b方等于c方
#             if a+b+c==1000 and a**2 + b**2 == c**2:
#                 print("a,b,c:%d, %d, %d" % (a,b,c))
# end_time = time.time()
# print("times:%d" % (end_time - start_time))
# print("finished")

#第二种思想: 有了a和b肯定c就可以固定了.那么可以改成以下代码实现起来效率有很大提高

start_time = time.time()
#时间复杂度：
#T(n) = O(n*n*10) = O(n^2)
for a in range(0, 1001):
    for b in range(0, 1001-a):
        c = 1000-a-b
        if a**2 + b**2 == c**2:
            print("a,b,c:%d, %d, %d" % (a,b,c))

end_time = time.time()
print("elapsed:%f" %(end_time - start_time))
print("complete!")

#分析时间复杂度
"""
    1.外层循环要执行的次数
    T = 1000 * 1000 * 1000 * 2

    2.如果将总数改成2000
    T = 2000 * 2000 * 2000 * 2
    T = N*N*N*2

    3.T(n) = n^3 * 2   n的三次方乘以2
    那么我们将T(n)称作时间复杂度

    4.上面提到的时间频度T(n)中，n称为问题的规模，当n不断变化时，时间频度T(n)也会不断变化。
    但有时我们想知道它变化时呈现什么规律，为此我们引入时间复杂度的概念。一般情况下，
    算法中基本操作重复执行的次数是问题规模n的某个函数，用T(n)表示，
    如果存在一个整数函数g和实常数c>0，使得对于充分大的n总有T(n)<=c*g(n)，
    就说函数g是T(n)函数的一个渐近函数（忽略常数），记为T(n)=O(g(n))，
    它称为算法的渐进时间复杂度，简称时间复杂度。这种用O( )来体现算法时间复杂度的记法，我们称之为大O表示法。

    大O表示法实际就是去掉T(n)函数的最高阶项系数、低阶项和常数项，只保留最高阶项。如T(n)函数为5n3 + 3n + 5，
    使用大O表示法则时间复杂度为O(n3)。


    5.对于算法的效率衡量，最重要的是其数量级和趋势，这些是分析算法效率的主要部分。
    而计量算法基本操作数量的规模函数中那些常量因子可以忽略不计。
    例如，可以认为3n2和100n2属于同一个量级，如果两个算法处理同样规模实例的代价分别为这两个函数，
    就认为它们的效率“差不多”，都为n2级。

结论:由此可见，我们尝试的第二种算法要比第一种算法的时间复杂度好的多。
"""


#4.最坏时间复杂度
"""
     分析算法时，存在几种可能的考虑：
        算法完成工作最少需要多少基本操作，即最优时间复杂度
        算法完成工作最多需要多少基本操作，即最坏时间复杂度
        算法完成工作平均需要多少基本操作，即平均时间复杂度
     我们主要关注的是算法的最坏情况,亦即最坏时间复杂度
"""

#5.时间复杂度的几条基本计算规则
"""
    基本操作，即只有常数项，认为其时间复杂度为O(1)
    顺序结构，时间复杂度按加法进行计算
    循环结构，时间复杂度按乘法进行计算
    分支结构，时间复杂度取最大值
    判断一个算法的效率时，往往只需要关注操作数量的最高次项，其它次要项和常数项可以忽略
    在没有特殊说明时，我们所分析的算法的时间复杂度都是指最坏时间复杂度


"""