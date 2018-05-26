# 引用:数据内存中的地址,也可以说内存地址,引用就是内存地址
# 引用:指向都说的内存地址
"""
定义变量a存储的数据就是10,变量是存储数据的容器,也可以说变量是存储
数据在内存中的地址,变量保存的是数据内存地址



"""
a = 10
result = id(a)

print(result,hex(result))
print(a)

# b保存的是a存储的内存地址,所以两个是一样的
b = a
print(result,hex(result))

print(b)



# 创建列表

my_list = [1,2]
my_list1 = my_list

my_list_address = id(my_list)
my_list1_address = id(my_list1)
print(hex(my_list1_address), hex(my_list_address))
print(my_list, my_list1)