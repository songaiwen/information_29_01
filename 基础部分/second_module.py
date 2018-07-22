def sum_num(num1, num2):
    return num1 + num2


# 提示： 快捷方式打印 ‘main’
# 判断当前模块是否是主模块
if __name__ == "__main__":
    # 测试功能代码
    result = sum_num(2, 4)
    print(result)


# 提示： 运行那个模块，那么这个模块就是主模块，也可以成程序入口的模块
# 查看当前模块名
print(__name__)