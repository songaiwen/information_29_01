#递归函数：在函数里面调用当前函数本身就是地柜函数
result = 1
for value in range(3, 0, -1):
    result *= value

print(result)

"""
3! = 3* 2!
2! = 2 * 1!
1! = 1

"""

# 计算3阶乘函数
def calc_num(num):
    if num == 1:
        return 1
    else:
        return num * calc_num(num - 1)

result = calc_num(3)
print(result)


# 递归调用有上限控制
# 获取默认的递归次数
import sys
count = sys.getrecursionlimit()
print(count)

# 设置递归次数
sys.setrecursionlimit(1100)
count = sys.getrecursionlimit()
print(count)

# 将上面的函数计算数写成1000，测试结果如下
result = calc_num(1000)
print(result)