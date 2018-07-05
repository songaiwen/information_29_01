#1.函数的定义
def test():
    print("in test")
#函数的调用
test()
#函数的引用,函数test将对象赋值给t,两个同时指向同一片空间
t = test
#函数名只是一个 指向函数代码空间的对象
#那么也可以使用t来调用函数
t()
#两个id是一样的说明指向同一片内存空间
print(id(t))
print(id(test))

#2.闭包
#定义函数test,解释器向下走,并没有执行,等待函数调用的时候才执行打印print
def test(num1):
    #打印出in test func
    print("in test func")
    #在函数内部又定义一个函数test_in,同样不执行,等待函数调用时再执行打印功能
    def test_in(num2):
        print("in test_in func %d" % (num1 + num2))
    #将内部函数test_in返回给外部函数
    return test_in
#将指向函数代码空间的test对象赋值给t,那么执行t的时候两个函数都将被执行
t = test(999)
t(1)
#总结闭包三个特点:
    #1.外部函数内部定义了内部函数
    #2.外部函数总是返回内部函数的引用
    #3.内部函数可以使用外部函数提供的环境变量
    # 定义:内部函数及其使用的环境变量(num1就是环境变量)构成的整体

#需求:求直线方程
#没有闭包的情况
"""
def line(k,x,b):
    print("y=%d" % (k*x + b))
#结果y = 11
line(1, 10, 1)

"""
#使用闭包的方法
def line(k, b):
    def inner(x):
        print("y = %d" % (k*x+b))
    return inner
#返回内部函数的引用赋值给line2,参数1传给k, 参数2传给b
line2 = line(1,2)
#外部函数的引用在调用的时候传递的99 实际是传递给内部函数inner的 即x=99
line2(99)


#3.修改环境变量
def line(k, b):
    # #python2中没有nonlocal的关键字方法,只能用曲线救国的方法修改环境变量k的值
    # data = [k]
    def inner(x):
        #python3中,用nonlocal修改环境变量的关键字
        nonlocal k
        k += 1
        print("y = %d" % (k*x+b))
        #这种方式py2和py3都可以使用的方法
        # data[0] += 1
        # print("y = %d" % (data[0] * x + b))
    return inner
line2 = line(1,2)

#需求:分析一个求平均值的闭包案例
#创建一个求平均数的函数
def make_avg():
    #创建一个空的列表
    data = list()
    #定义内部函数,计算平均值并返回
    def addnumber(value):
        #修改外部函数中的变量,向里面添加value的值
        data.append(value)
        #将列表中的数据求和
        total = sum(data)
        #用求和的结果除以len出列表中数据的个数去个平均值并返回
        return total/len(data)
    #返回内部函数的引用给外部函数
    return addnumber
my_avg = make_avg()
print(my_avg(100)) #100.0
print(my_avg(200)) #150.0


#4.装饰器
#先理解一段代码,定义一个函数,并将函数引用赋值给f ,则调用f的时候也可以执行代码
def foo():
    print("in foo")
f = foo
f()
#如果将foo这个对象重新指向另个函数的代码快,那么此函数就执行新的代码功能了
foo = lambda x : x + 1
#因为匿名函数需要参数所以调用的时候需要传入一个参数
result = foo(5)
print(result)
#总结:函数名是一个指向了函数代码的对象,此对象还可以指向别的代码空间
#装饰的概念
#需要扩展的功能是抽象的,是容易变化的,
#想要在登陆f1时候验证,那么用验证的函数包含f1函数
def yanzheng(func):
    print("验证1------------")
    func()
def f1():
    print("in f1")
#上层应用开发
# f1()
#但是我们本应该去调用f1函数的,却变成了调用yanzheng函数了.并不是很理想,所以
#使用闭包的概念来完善此函数
yanzheng(f1)

#用闭包函数修改上面功能
#定义验证函数,形参是func
def yanzheng(func):
    #定义验证的内部函数
    """
    装饰器函数特点:
    1.满足闭包所有要求
    2.只有一个参数就是被装饰的函数的引用
    使用装饰器的语法
    @装饰器函数
    """
    def inner():
        print("验证开始----------")
        #因为f1作为参数参数穿进来,此时执行func就等于执行f1函数
        func()
        print("验证完成")
    #返回内部函数引用给外部函数,谁调用的给谁
    return inner

#@装饰器函数+下面的函数就成了一个装饰器函数
@yanzheng
def f1():
    print("in f1")
#调用yanzheng函数的时候把f1当做参数传给func,得到内部函数引用并用f1保存
#这一步是对f1功能进行的扩展,可以当做底层需要做的,我们需要用语法糖装饰
#f1就是被装饰的函数
# f1 = yanzheng(f1) #那么就用语法的形式变成@yanzheng写在f1函数上面
#那么此时调用f1函数就能实现整个验证
f1()
print("==============================================")
#5.装饰器的功能
    #1.引入日志
    #2.函数执行时间统计
    #3.执行函数前预备处理
    #4.执行函数后清理功能
    #5.权限校验场景
    #6.缓存
#需求:实现能够获取函数运行时间的装饰器
import time
def gettime(func):
    def inner():
        begin = time.time()
        func()
        end = time.time()
        print("函数的运行时间%f秒" % (end - begin))
    return inner
@gettime
def f1():
    print("in f1")
    for i in range(3):
        time.sleep(0.5)
@gettime
def f2():
    print("in f2")
    for i in range(3):
        time.sleep(0.5)
f1()
f2()


#5.带有参数和返回值的装饰器
def gettime(func):
    """装饰器函数"""
    def inner(*args, **kwargs):
        """内层函数"""
        #将所有的位置参数,关键字参数全部接受
        begin = time.time()
        #将所有位置参数和关键字参数原封不动的传入到内部调用函数中
        ret = func(*args, **kwargs)
        end = time.time()
        print("函数的运行时间%s" % (end - begin))
        #先把上面的函数用一个变量容器装起来,等所有的事情都做完了再返回
        return ret
    return inner

@gettime
def f3(number):
    print("in f3 %d" % number)
    for i in range(3):
        time.sleep(0.5)
    #如果装饰器函数中没有返回值的话,这个地方的返回在下面调用打印的时候是不能被打印出来的
    #所以在上面的装饰器函数内部把函数需要做的事情都做完以后用一个变量ret保存起来,然后在最后的位置返回结果
    #再在下面调用的时候打印出来就可以了
    return 10086
@gettime
def f4(number1,number2):
    print("in f4 %d" % (number1 + number2))
    for i in range(3):
        time.sleep(0.5)
    return 520
print(f3(100))
print(f4(200,300))


#6.装饰器工厂函数
def get_run_time(flag):
    """装饰器工行函数"""
    def gettime(func):
        """装饰器函数"""
        def inner(*args, **kwargs):
            begin = time.time()
            ret = func(*args, **kwargs)
            end = time.time()
            if flag == 1:
                print("函数运行时间是%d" % int(end-begin))
            else:
                print("函数的运行时间%f" % (end-begin))
            return ret
        return inner
    return gettime
@get_run_time(1)
def f5(number3):
    print("in f5 %d" % number3)
    for i in range(3):
        time.sleep(2)
    return 521
@get_run_time(0)
def f6(number4, number5):
    print("in f6 %d" % (number4 + number5))
    for i in range(5):
        time.sleep(1)
    return 1314
#装饰器工厂函数的目的:装饰器函数只有一个参数--是被装饰的函数的引用
#装饰器工厂函数,就收额外的参数--遗传--->给最内部的函数使用,进行判断或者其他操作
#使得f5得到的结果是整数,而f6由于是0 ,在内部判断执行else功能得到的是浮点数结果
print(f5(9999))
print(f6(789,567))


#7.类装饰器
class MyClass(object):
    """装饰器类"""
    def __init__(self, func):
        #保存一个被装饰的函数的引用
        self.__func = func

    def __call__(self, *args, **kwargs):
        print("正在开始验证")
        #调用上面的函数
        self.__func()
        print("退出")
@MyClass
#这个类能实现装饰器功能就是类装饰器
#这个等价于f7 = MyClass(f7),而此时上面不能接受参数,需要重写init方法
#实例对象 = 类名()
def f7():
    print("正在剁手")
#callable(对象)判断对象是否是可调用对象:形式  对象()
#函数()   匿名函数对象()    方法()  类对象()  实现call方法的-->实例对象()
f7()


#8.多个装饰器装饰一个函数
def makeBold(func):
    """装饰器函数,功能是给函数外面加一个b标签加粗"""
    def inner():
        return "<b>" + func() + "<b>"
    return inner

def makeItalic(func):
    """装饰器函数,功能是给函数外面加一个i标签倾斜"""
    def inner():
        return "<i>" + func() + "<b>"
    return inner
@makeItalic
@makeBold
#想要先实现哪个装饰器就将装饰器写在下面,最后一个实现的在上面
def hello1():
    return "hello world"
print(hello1())

#9.flask中的route的使用的唯一目的是为了添加路由


















