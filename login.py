num1 = 10
# 字典的常见操作

my_dict =  {"name": "李广", "age": 20, "sex": "男"}
# 1.len
count = len(my_dict)
print(count)

# 2.keys:获取字典中的key值,keys需要通过list转换获取列表
keys = my_dict.keys()
print(list(keys))

#3.values:获取字典中的value值
values = my_dict.values()
print(list(values))

# 4.items 获取字典中每项键值对,封装到元祖里面
items = my_dict.items()
print(items)
print(list(items))