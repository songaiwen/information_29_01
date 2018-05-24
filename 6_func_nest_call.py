# 函数的嵌套调用:在函数里面调用其他函数的操作就是函数的嵌套调用
def print_info1():
    print("开始执行 print_info1")

    print("好好学习，天天向上")

    print("结束执行 print_info1")

def print_info2():
    print("我的代码刚开始,就需要去调用print_info1的代码")

    print_info1()

    print("调用完了print_info1的代码就结束了")

print_info2()


# 函数嵌套:在函数里面再定义函数
def shou_info():
    # 在函数里面的函数成为子函数
    def print_num():
        print("123456789")
    print_num()

shou_info()

# demo1,把一个苹果放到冰箱里面

def use_bx(eat):
    def open_bx():
        print("打开冰箱")

    def input_eat(eat):
        print("放入%s"%eat)

    def close_bx():
        print("关闭冰箱")

    open_bx()
    input_eat(eat)
    close_bx()

use_bx("苹果")


# demo2,打印10条横线

def print_one_line():
    print("-" * 30)

def print_more_line(num):
    for i in range(num):
        print_one_line()

print_more_line(10)

# demo3,设计一个函数求三个数的和

def sum_num(num1, num2, num3):
    result = num1 + num2 +num3
    return result
result = sum_num(5,15,20)
print(result)

def avg_num(num1, num2, num3):
    result = sum_num(num1, num2, num3)
    result = result / 3
    return result

result = avg_num(5, 15, 20)
print(result)


# 局部变量和全局变量
def print_num():
    num = 55
    print(num)

# 局部变量在函数里面使用的变量,在函数外面不能使用
#局部变量的作用是在函数里面临时保存一些数据,函数调用完成以后局部变量会被释放
# return返回的值,在会在外界使用完成以后才会释放
print_num()


# 全局变量,在不同函数里面页可以使用的变量,也可以理解为在函数外面定义的变量

num = 10

def show_info():
    # 局部变量,只不过名字和全局变量相同
    # 特点,先从局部找,找到了用局部变量,找不到再去全局找,找到了用全局,找不到崩溃
    # 就近原则使用
    # num = 20
    # print(num)

    global num
    num = 30
    print(num)

# 由于show_info内部已经将全局变量的值改变了,所以show_info2输出的就是修改后的值
def show_info2():
    print(num)

show_info()
show_info2()


















































