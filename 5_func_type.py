# 1.无参数无返回值
def show_info():
    print("代码速度6666")

# 2.无参数有返回值
def show_desc():
    return "hello world"

# 3.有参数无返回值
def show_num(num1, num2):
    print(num1, num2)

# 4.有参数有返回值
def show_person_info(name, age):
    return "我的姓名是:%s , 年龄是:%d" % (name, age)
# 调用的是 1
show_info()

# 2
result = show_desc()
print(result)

# 3
show_num(1111,2222)

# 4
result = show_person_info("宋雨希", 25)
print(result)
