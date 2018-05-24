my_dict = {"name": "李广", "age": 20, "sex": "男"}

# 默认遍历字典获取的每一个key
for key in my_dict:
    value = my_dict[key]
    print(key, value)

print("------------------------------------------")
# 遍历所有的value值
for value in my_dict.values():
    print(value)

print("------------------------------------------")

# 遍历所有的key值
for key in my_dict.keys():
    print(key)

print("------------------------------------------")

# 遍历每项数据的key和value值
for item in my_dict.items():
    print(item[0],item[1])

print("------------------------------------------")

# 拆包获取元祖里面的数据
for key, value in my_dict.items():
    print(key, value)
print("------------------------------------------")

# enumerate函数获取对象中成员下表和成员
for index, value in enumerate("hello"):
    print(index, value)

print("------------------------------------------")

for index, value in enumerate((1,4,5,8,9)):
    print(index, value)

print("------------------------------------------")

# 获取遍历的是第几个键值对的下表,并且通过key获取value

for index, item in enumerate(my_dict.items()):
    key, value = item
    print(index, key, value)

num1 = 10
