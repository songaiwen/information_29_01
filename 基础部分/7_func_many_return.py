"""
总结:函数里面多个return语句语法上没有问题
但是代码执行到return语句以后,函数执行结束,会回到函数调用的地方,return后面的代码不会执行

"""

def return_more_value():
    print("1111111111")
    return 1, 2
    # 如果不想外界修改返回的数据可以使用元祖 ,要修改 的话可以使用列表或者是字典
    # return{"name":"杨幂","age":18}  #不会执行


result = return_more_value()
print(result,type(result))


"""
缺省参数:可选参数,如果给参数传值,那么使用传入过来的值, 否则使用默认值
缺省参数不能放在普通参数前面,缺省参数后面还可以使用缺省参数


"""


def sum_num(num1, num2=10):
    return num1 + num2

result = sum_num(1)
print(result)


# 显示学生信息的功能函数
def studen_info(name, age):
    print("姓名:",name, "年龄:",age)

"""
使用位置参数调用函数:位置参数一定按着参数定义的顺序去传参



"""
studen_info("songjiaying",25)

#使用关键字参数调用函数,根据函数的参数名设置参数值,不会要求按着一定顺序传参
studen_info(age=20, name="songyuxi")


"""
不定长参数:不确定用户传入多少个参数,可能是0个1个或者多个
分为,不定常位置参数,和不定常关键字参数
**kargs表示可以接收不定常关键字参数


"""


def show_info(**kwargs):
    print(kwargs,type(kwargs))
    #**kwargs:把关键字参数封装在字典里面,类型就是字典
    for key,value in kwargs.items():
        print(key,value)


    result = kwargs["a"]
    print(result)

show_info(a=1,b=2)


"""
*args可以接收不定常位置参数

"""

def sum_num(*args):
    #*args把位置参数封装到元组里面,类型就是元组
    print(args,type(args))

    result = 0
    for value in args:
        result += value

    return result

result = sum_num(1,2)
print(result)



































