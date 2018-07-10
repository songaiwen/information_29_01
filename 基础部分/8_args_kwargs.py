# 交换两个变量的值
num1 = 10
num2 = 20

# 方法1可以使用临时变量
num3 = num1
num1 = num2
num2 = num3

print(num1,num2)

# 方法2可以给变量赋值,python特有的
num1,num2 = num2,num1
print(num1, num2)

