"""
1.计算机的文件： 计算机文件是以硬盘为载体存储计算机上信息数据的集合，使用文件可以做到永久保存
学习文件的目的： 把程序中数据保存到文件里面，可以防止数据的丢失
提示： 少量数据可以保存在文件里面，如果信息量比较大可以使用数据库

"""
"""
2.创建文件对象:
    第一个参数是打开的文件名
    第二个参数是访问文件的模式:w表示可写， 如果文件不存在那么先创建文件然后再写入数据，如果文件存在先清空数据然后再写入
    查看编码方式，在window上文件默认的编码格式cp936 其实就是GBK
    提示： 在mac和乌班图上编码格式不需要指定，因为默认是就是utf-8格式
"""
file = open("text.txt", "w", encoding="utf-8")
print(file.encoding)
file.write("哈哈今天学习了文件操作了")
file.close()

"""
3.文件的访问模式
"""
#1.r 只读模式:不能写入数据,注意点:r模式读取数据文件必须存在,否则崩溃, 不支持写入文件
file = open("text.txt", "r", encoding="utf-8")
result = file.read()
#读取数据,一次性读取文件里面的所有数据
print(result)
file.close()

#2.w:只写，不能读取数据，注意点： 如果文件不存在会先创建文件，然后再写入数据，如果文件存在那么先清理源文件里面的数据，然后在写入
#不执行读取数据的操作
file = open("text1.txt", "w", encoding="utf-8")
file.write("我是进来玩耍的呢")
file.close()

#3.a:追加,不能读取数据， 注意点： 如果文件不存在先创建文件，然后再写入，如果文件存在在原有数据的后面追加写入数据
#不执行读取数据的操作
file = open("text1.txt", "a", encoding="utf-8")
file.write("我是追加进来的内容")
file.close()

#4.rb:以二进制方式读取数据
#提示： 文件访问模式里面如果带有b模式，不需要指定编码格式，因为数据读取出来或者写入都需要进行解码和编码
#部支持写入操作
file = open("text1.txt", "rb")
result = file.read()
#读取二进制数据并进行解码操作
print(result.decode("utf-8"))
file.close()

#5.wb:以二进制的方式写入数据
#注意点：如果文件不存在先创建文件再写入，如果文件存在那么先清空原有数据然后在写入
file = open("text2.txt", 'wb')
content = "wb模式而是可以创建文件然后再写入"
#把字符串进行utf-8的编码转成二进制
content_data = content.encode("utf-8")
print(content_data)
file.write(content_data)
file.close()

#6.ab:以二进制方式追加写入数据
#注意点：如果文件不存在先创建文件再写入，如果文件存在那么会在原有数据基础上往后追加写入
file = open("test3.txt", "ab")
content = "ab模式也是可以创建文件然后在写入"
# 把字符串进行utf-8的编码转成二进制
content_data = content.encode("utf-8")
print(content_data)
file.write(content_data)
file.close()

#7.r+： 读取和写入， 注意点：r+模式操作文件必须存在
#r模式：默认是从头开始读取数据
file = open("text1.txt", "r+", encoding="utf-8")
# 读取数据
result = file.read()
print(result)
file.write("hahahaahh,什么事情都没有做呢")
file.close()

#8.w+: 写入和读取 注意点： 如果文件不存在先从创建文件然后再写入数据，如果文件存在那么先清空原有数然后再写入
file = open("text2.txt", "w+", encoding="utf-8")
# 写入
file.write("哈哈,我就是进来看看没什么事情")
# 设置文件指针，文件指针可以理解成光标
file.seek(0) # 把文件指针设置到文件的开始位置
# 读取数据
result = file.read()
print(result)
# 关闭文件
file.close()

#9.a+: 追加写入和读取数据 注意点：如果文件不存在先从创建文件然后再写入数据，如果文件存在会在原有数据基础上往后追加写入的数据
file = open("text3.txt", "a+", encoding="utf-8")
# 写入
file.write("今天天气不错呢")
# 设置文件指针，文件指针可以理解成光标
file.seek(0) # 把文件指针设置到文件的开始位置
# 读取数据
result = file.read()
print(result)
# 关闭文件
file.close()

#10.rb+: 以二进制读取和写入数据, 注意点：文件必须存在
file = open("text1.txt", "rb+")
# 读取数据
result = file.read()
content = result.decode("utf-8")
print(content)
# 写入数据
file.write("哈哈，我又来写数据啦".encode("utf-8"))
# 关闭文件
file.close()

#11.wb+：以二进制方式写入和读取数据， 注意点：如果文件不存在先从创建文件然后再写入数据，如果文件存在那么先清空原有数然后再写入
file = open("test8.txt", "wb+")
# 写入数据
file.write("哈哈，我又来写数据啦".encode("utf-8"))
# 设置文件指针到文件开头
file.seek(0)
# 读取数据
result = file.read()
content = result.decode("utf-8")
print(content)
# 关闭文件
file.close()

#12ab+ : 以二进制方式追加写入和读取数据 注意点：如果文件不存在先从创建文件然后再写入数据，如果文件存在会在原有数据的基础上追加数据
file = open("test11.txt", "ab+")
# # 写入数据
file.write("哈哈，我又来写数据啦".encode("utf-8"))
# 设置文件指针到文件开头
file.seek(0)
# 读取数据
result = file.read()
content = result.decode("utf-8")
print(content)
# 关闭文件
file.close()

"""
3.文件的读写
"""
#1. 创建文件，写入数据
file = open("test12.txt", "wb")
# 写入数据
content = "哈哈哈，我是要测试的"
# 按照utf-8编码格式把数据转成二进制
content_data = content.encode("utf-8")
file.write(content_data)
# 关闭文件
file.close()

# 2.读取文件里面全部数据
file = open("text2.txt", "r", encoding="utf-8")
result = file.read()
print(result)
file.close()

# 3.读取指定长度的数据
file = open("test12.txt", "r", encoding="utf-8")
result = file.read(3) # r模式read里面的参数是读取数据的长度
print(result)
file.close()

#4.
file = open("text2.txt", "rb")
# 在utf-8的编码下，一个汉字占用三个字节，一个字母占用1个字节
result = file.read(3)  # rb模式read里面的参数是读取的字节的长度
# 对二进制数据进行utf-8的解码
# errors表示如果按照utf-8进行解码， 解码不出来可以忽略特殊字符，保证程序不崩溃
content = result.decode("utf-8", errors="ignore")
print(content)
file.close()

#5.读取一行数据
file = open("text2.txt", "r", encoding="utf-8")
# 读取一行数据
result = file.readline()
print(result)
file.close()

# 6.读取多行数据
file = open("test9.txt", "r", encoding="utf-8")
# 读取一行数据
result = file.readlines()
print(result)
for value in result:
    print(value)
file.close()

"""
4.模拟大文件的读取
"""
# 模拟读取大文件的操作
file = open("test4.txt", "rb")
while True:
    # 读取数据
    file_data = file.read(1024) # 读取最大字节数据1024
    # if len(file_data) > 0:
    if file_data:
        # 读取到数据
        # errors="ignore": 忽略解码不成功的特殊字符
        file_content = file_data.decode("utf-8", errors="ignore")
        print(file_content)
    else:
        print(file_data)
        break
# 关闭文件
file.close()

"""
5.文件拷贝
"""
import os

# 接收用户输入文件名
copy_file_name = input("请输入要拷贝的文件名:")
# 判断文件是否存在
is_exists = os.path.exists(copy_file_name)
if is_exists:
    # 文件存在，进行文件的拷贝
    # "test.txt" => "test[复件].txt"
    # 1. 根据点进行分割，获取文件名和文件的后缀，完成字符串的拼接 copy_file_name.split(".")
    # 2. 根据指定字符串，以指定字符串为中心，完成字符串三份的分割
    file_name, point_str, extension_name = copy_file_name.partition(".")
    # 生成复制后的文件名
    dest_file_name = file_name + "[复件]" + point_str + extension_name
    # 创建目标文件对象，完成数据的写入
    # dest_file = open(dest_file_name, "wb")

    # 扩展： 拷贝到桌面上
    # \:表示转义字符，两个反斜杠表示一个真正的反斜杠字符
    dest_file_path = "C:\\Users\\Apple\\Desktop\\" + dest_file_name
    print(dest_file_path)
    dest_file = open(dest_file_path, "wb")
    # # 创建文件对象， 获取源文件的数据
    source_file = open(copy_file_name, "rb")
    # 循环读取文件里面的数据
    while True:
        # 读取文件数据
        source_file_data = source_file.read(1024)
        # 判断文件是否读取完成
        if source_file_data:
            # 获取到文件数据了, 把数据写入到新的文件
            dest_file.write(source_file_data)
        else:
            break
    # 关闭文件
    source_file.close()
    dest_file.close()
else:
    print("文件不存在")


"""
6.文件及文件夹的相关操作
"""
import os
import shutil
# 创建文件
file = open("test13.txt", "w", encoding="utf-8")
file.write("sdfja;sdfjk;ljasdf")
file.close()

# # 创建文件夹
# os.mkdir("AAA")
# 获取当前目录
# result = os.getcwd()
# print(result)
# # 切换目录
# os.chdir("AAA")  # AAA  ./AAA ,./表示当前目录，../表示上级目录
# result = os.getcwd()
# print(result)

# file = open("test13.txt", "w", encoding="utf-8")
# file.write("sdfja;sdfjk;ljasdf")
# file.close()

# 重命名
# os.rename("test13.txt", "test.txt")
# 修改文件夹, 注意路径和AAA路径的父目录
# os.rename("AAA", "BBB")

# 扩展：既改文件夹又改文件名
# os.renames("BBB/test.txt", "CCC/test1.txt")
# # 给指定目录创建文件夹
# os.mkdir("CCC/AAA")

# 删除空文件夹, 只能删除空文件夹
# os.rmdir("CCC/AAA")

# 获取指定路径文件列表信息
file_list = os.listdir("CCC")
print(file_list)

# 扩展：
# 删除文件夹及里面的所有文件
# shutil.rmtree("CCC")

# 获取文件的绝对路径, 绝对路径： 从根路径算起的就是绝对路径
my_path = os.path.abspath("test.txt")
print(my_path)
# 获取绝对路径的文件名
file_name = os.path.basename(my_path)
print(file_name)
# 获取文件名及文件后缀
file_name, extension_name = os.path.splitext(file_name)
print(file_name, extension_name)


"""
7.批量修改文件名
"""
import os
# 1. 思路 如果在默认路径下开发，获取AAA目录下的文件信息使用 os.listdir("AAA"),  遍历文件列表进行文件名的拼接，然后在重命名但是需要加上路径

# file_name_list = os.listdir("AAA")
#
#
# for file_name in file_name_list:
#     new_file_name = "{彬哥出品}-" + file_name
#
#     os.rename("AAA\\" + new_file_name,  "AAA\\" + file_name)

# 2. 思路，切换到AAA目录里面进行文件的重命名
os.chdir("AAA")
# 查看当前目录的文件信息
file_name_list = os.listdir(".") # os.listdir() 默认获取的当前目录的信息
print(file_name_list)

for file_name in file_name_list:
    # 生成新的文件名
    new_file_name = "{彬哥出品}-" + file_name
    print(new_file_name)
    # 重命名
    os.rename(file_name, new_file_name)


"""
8.学生管理系统文件版本
"""
import os

# 定义学生列表， 存储的学生字典信息
student_list = []
# 显示功能菜单
def show_menu():
    print("学生管理系统".center(20))
    print("1.添加学生")
    print("2.删除学生")
    print("3.修改学生")
    print("4.查询学生")
    print("5.显示所有学生")
    print("6.保存数据")
    print("7.退出")

# 添加学生
def add_student():
    # 接收用户输入学生信息
    name = input("请输入您的姓名:")
    age = input("请输入您的年龄:")
    sex = input("请输入您的性别:")
    # 把参数封装到字典
    student_dict = {}
    # 添加键值对
    student_dict["name"] = name
    student_dict["age"] = age
    student_dict["sex"] = sex
    # 添加到学生列表里面， 因为student_list 是可变类型，添加数据不会对内存地址进行修改，那么可以不需要加上global
    student_list.append(student_dict)
    '''
    # 总结: 加上global关键字表示要对全局变量的内存地址进行修改，如果内存地址不变可以不需要加上global
    global student_list
    # 如果不加global表示定义的是局部变量
    student_list = [{"name": "张三", "age": 20, "sex": "男"}]
    '''
# 删除学生
def remove_student():
    # 接收用户输入的学生序号
    num = input("请输入要删除学生的序号:")
    # 根据序号获取下标
    index = int(num) - 1
    # 控制下标的范围，防止越界
    if index >= 0 and index < len(student_list):
        # 根据下标删除学生信息
        del student_list[index]
    else:
        print("请输入合法序号!")

# 修改学生
def modify_student():
    # 接收用户输入的学生序号
    num = input("请输入要修改的学生的序号:")
    # 根据序号获取下标
    index = int(num) - 1
    # 控制下标的范围，防止越界
    if index >= 0 and index < len(student_list):
        # 根据下标获取学生信息
        student_dict = student_list[index]
        # 获取修改的信息
        new_name = input("请输入修改后的姓名:")
        new_age = input("请输入修改后的年龄:")
        new_sex = input("请输入修改后的性别:")
        # 修改键值对
        student_dict["name"] = new_name
        student_dict["age"] = new_age
        student_dict["sex"] = new_sex
    else:
        print("请输入合法序号!")

# 查询学生
def query_student():
    # 获取用户的输入的信息
    name = input("请输入要查询学生姓名:")
    # 遍历学生列表获取字典里面name的value值进行比较
    for index, student_dict in enumerate(student_list):
        if student_dict["name"] == name:
            print("找到了，信息如下:")
            print("序号:%d 姓名:%s 年龄:%s 性别:%s" % (index + 1, student_dict["name"],
                                               student_dict["age"], student_dict["sex"]))
            # 找到了就需要在往后面循环进行判断
            break
    else:
        # 注意点: 执行break不会执行else，否则执行也就是没有找到人
        print("没有这个人信息")

# 显示所有学生
def show_student_list():
    for index, student_dict in enumerate(student_list):
        print("序号:%d 姓名:%s 年龄:%s 性别:%s" % (index + 1, student_dict["name"],
                                           student_dict["age"], student_dict["sex"]))

# 保存数据(全局变量的列表数据)到文件
def save_data():
    # 获取文件对象
    file = open("student_list.data", "w", encoding="utf-8")
    # 把列表转成字符串类型
    student_list_str = str(student_list)
    # print(student_list_str, type(student_list_str))
    # # 写入数据（全局变量的列表数据写入到文件）
    file.write(student_list_str)
    # 关闭文件
    file.close()

# 加载本地文件数据
def load_data():
    is_exists = os.path.exists("student_list.data")
    if is_exists:
        # 存在，加载本地文件数据
        file = open("student_list.data", "r", encoding="utf-8")
        # 读取文件数据
        student_list_str = file.read()
        # print(student_list_str, type(student_list_str))
        # 获取字符串中原始数据类型，得到是列表
        new_student_list = eval(student_list_str)
        # 声明要修改全局变量
        # global student_list
        # student_list = new_student_list
        # 在原有数据的基础上修改全局变量，内存地址不变，可以不需要使用global
        student_list.extend(new_student_list)
        # print(new_student_list, type(new_student_list))
        # list转字符串这样是把字符串中每一个元素放到列表中，不符合我们的需要
        # result = list("[{name:'zs'}]")
        # print(result)
        # 关闭文件
        file.close()

# 程序入口函数
def run():
    # 加载本地文件数据
    load_data()
    # 循环接收用户输入的指令
    while True:
        # 显示功能菜单
        show_menu()
        # 接收用户输入的指令
        menu_option = input("请输入功能选项:")
        if menu_option == "1":
            # 添加学生
            add_student()
        elif menu_option == "2":
            # 删除学生
            remove_student()
        elif menu_option == "3":
            # 修改学生
            modify_student()
        elif menu_option == "4":
            # 查询学生
            query_student()
        elif menu_option == "5":
            # 显示所有学生
            show_student_list()
        elif menu_option == "6":
            # 保存数据
            save_data()
        elif menu_option == "7":
            # 退出
            # pass
            # exit()
            break
        else:
            print("请输入合法功能选项!")
# 执行程序入口函数
run()


