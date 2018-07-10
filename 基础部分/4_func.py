#函数定义的格式
"""
def 函数名(参数列表...):
    函数实现代码

"""
# demo

def show_info():
    print("社会我希姐,人狠话不多")

# 调用函数
show_info()


# 函数文档说明
def sum_num(num1, num2):
    """
    完成两数相加的功能
    """
    result = num1 + num2

    print(result)


# 查看函数的文档说明
help(sum_num)


# 完成两数相加的功能函数
def sum_num(num1, num2):  # 定义的带有参数的函数，参数放到小括号里面
    print("num1:", num1 , "num2:", num2)
    result = num1 + num2
    print(result)


# 调用函数 =》 函数名(参数,xx)
sum_num(1, 2)

# 函数返回值
def sum_num(num7, num8):
    print(num7, num8)
    result = num7 + num8
    return result
# 处理返回值,用变量保存
result = sum_num(2,4)
print(result)