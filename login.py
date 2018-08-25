# num1 = 10
# # 字典的常见操作
#
# my_dict =  {"name": "李广", "age": 20, "sex": "男"}
# # 1.len
# count = len(my_dict)
# print(count)
#
# # 2.keys:获取字典中的key值,keys需要通过list转换获取列表
# keys = my_dict.keys()
# print(list(keys))
#
# #3.values:获取字典中的value值
# values = my_dict.values()
# print(list(values))
#
# # 4.items 获取字典中每项键值对,封装到元祖里面
# items = my_dict.items()
# print(items)
# print(list(items))
#
# num2 = 20
#
# num3 = 30
# num4 = 40

# s = 'abc'
# print(type(s))
# #str编码变为bytes类型
# b = s.encode
# print(type(b))

# b = b'abc'
# print(type(b))
# #bytes类型解码成为str类型
# s = b.decode()
# print(type(s))


def extendlist(val, list=[]):
    list.append(val)
    return list


list1 = extendlist(10)

list2 = extendlist(123, [])
list3 = extendlist("a")
print('list1=%s' %list1)
print("list2=%s" % list2)
print("list3 = %s" % list3)

# def multipliers():
#     return [lambda x : i * x for i in range(4)]
# print [m(2), for m in multipliers()]



















