# 匿名函数：不使用def关键字定义的函数就是匿名函数，匿名函数也是函数，可以完成类似比较简单的
# 功能函数，简化普通函数的作用
# demo1定义普通函数计算两个数相加
def sum(num1,num2):
    return num1 + num2
result = sum(1, 2)
print(result)

# demo2 匿名函数
func = lambda num1, num2 : num1 + num2
result = func(1, 2)
print(result)

# 匿名函数还可以结合if判断使用
func = lambda x: True if x %2 == 0 else False
result = func(1)
print(result)

# 匿名函数还可以作为其他函数的参数，另外def函数也可以作为其他函数的参数
def show_info(function):
    print(function)
    num1 =1
    num2 =2
    result = function(1, 2)
    return result

func = lambda num1, num2:num1+num2
result = show_info(func)
print(result)


# 匿名函数的应用场景

my_list = [{"name":"syx","age":25,},{"name":"sjy","age":21}]
my_list.sort(key=lambda x: x["age"], reverse=True)
print(my_list)

my_list.sort(key=lambda x: x["name"])
print(my_list)


# 给程序传参
import sys

# 获取给程序传入的参数

params_list = sys.argv
# 想要获取参数列表后面的值，需要判断参数列表长度是否大于1，如果大于1表示至少2个
if len(params_list) > 1:
    # 从1下表开始，获取到最后一个小标
    result = params_list[1:]
    print(result)
print(params_list, type(params_list))