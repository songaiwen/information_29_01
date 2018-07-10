# 可变类型:在原有数据的基础上可以对数据进行修改(添加或者删除或者修改),修改后内存地址不变
# 例如字典,列表,集合
my_dict = {"name":"syx", "age":25}
print(id(my_dict))

my_dict["name"] = "sjy"
print(id(my_dict))

my_list = [1,2,3,4,5]
print(id(my_list))

my_list[0] = 6
print(id(my_list))

my_set = {7,8,9}
print(id(my_set))

my_set.add(10)
print(id(my_set))

#
# 不可变类型:不能在原有数据的基础上对数据进行修改
# 例如数字,字符串,元组

my_num = 1
print(id(my_num))
my_num = 2
# 这个不是修改数据,是修改变量对应的内存地址
print(id(my_num))

my_str = "hello"
print(id(my_str))
# my_str[0] = "H"
# 此时会报错,告诉我们字符串是部支持修改的
# print(id(my_str))

# 在python里面所有的传递都是应用传递,也可以说是内存地址传递
def show_info(info):
    print(id(info))

    info += info

    print(id(info), info)

my_list = [1,2]
print(id(my_list), my_list)

show_info(my_list)

