# # 1.无参数无返回值
# def show_info():
#     print("代码速度6666")
#
# # 2.无参数有返回值
# def show_desc():
#     return "hello world"
#
# # 3.有参数无返回值
# def show_num(num1, num2):
#     print(num1, num2)
#
# # 4.有参数有返回值
# def show_person_info(name, age):
#     return "我的姓名是:%s , 年龄是:%d" % (name, age)
# # 调用的是 1
# show_info()
#
# # 2
# result = show_desc()
# print(result)
#
# # 3
# show_num(1111,2222)
#
# # 4
# result = show_person_info("宋雨希", 25)
# print(result)


s = 'Hello World!'

print(s[4])


print(s[:]) # 取出所有元素（没有起始位和结束位之分），默认步长为1

print(s[1:]) # 从下标为1开始，取出 后面所有的元素（没有结束位）

print(s[:5])  # 从起始位置开始，取到 下标为5的前一个元素（不包括结束位本身）

print(s[:-1]) # 从起始位置开始，取到 倒数第一个元素（不包括结束位本身）

print(s[-4:-1]) # 从倒数第4个元素开始，取到 倒数第1个元素（不包括结束位本身）

print(s[1:5:2]) # 从下标为1开始，取到下标为5的前一个元素，步长为2（不包括结束位本身）

# python 字符串快速逆置
print(s[::-1])  # 从后向前，按步长为1进行取值


testStr = "haha nihao a \t heihei \t woshi nide \t hao \npengyou"
result = testStr.split()
print(result)