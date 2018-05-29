# 列表推导式：也成列表生成是，通过for循环快速生成创建的列表
my_list1 = [value for value in range(5)]
print(my_list1,type(my_list1))

my_list2 = [value for value in range(1, 20)]
print(my_list2, type(my_list2))

my_list3 = [value for value in range(1, 20, 2)]
print(my_list3,type(my_list3))


# 列表生成生成式还可以添加if判断

my_list4 = [value for value in range(1, 20) if value % 2 == 0]
print(my_list4, type(my_list4))

# 使用列表生成式创建元祖列表
my_list5 = [(value1, value2) for value1 in range(3) for value2 in range(3)]
print(my_list5, type(my_list5))

my_list6 = [(value3, value4, value5) for value3 in range(3) for value4 in range(3) for value5 in range(3) ]
print(my_list6)


# set集合：数据的集合，特点是无序的，集合里面没有重复的数据 ，可以添加深处元素，但是不能
# 根据下标修改获取根据下标获取元素

# 创建空的集合
# {}表示的是字典类型，不是set集合类型
my_set1 = {}
print(type(my_set1))

# 通过set类型创建的对象就是一个空的集合

my_set = set()
print(type(my_set))

# 查看变量保存的内存地址
print(id(my_set))
print(my_set)
# 添加元素,通过查看添加前后的内存地址，没有变化，说明是添加元素是不会改变内存地址的
my_set.add(1)
print(my_set)
print(id(my_set))

# 删除集合中的元素有两种方式
# 方式1
# my_set.remove(2)#删除的元素如果没有在集合里面会崩溃
# print(my_set)

# 方式2
my_set.discard(2)
print(my_set)#如果元素在集合里面那么删除元素，如果不在，就不会删除，页不会崩溃


# 遍历集合
my_set.add(2)
my_set.add(3)
my_set.add(4)
my_set.add(5)
my_set.add(6)

for value in my_set:
    print(value)

# 集合中的交集使用&
my_set2 = {1,3,5}
my_set3 = {3,5,6}
result = my_set2 & my_set3
print(result)

# 集合中的并集使用|
result1 = my_set2 | my_set3
print(result1)

# 差集使用-
result2 = my_set2 - my_set3
print(result2)

# 等差差集^
result3 = my_set2 ^ my_set3
print(result3)







