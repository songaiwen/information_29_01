# 定义学生列表，用来存储学生字典信息
student_list = []

# 显示功能菜单
def show_menu():
    print("学生管理系统".center(20))
    print("1.添加学生")
    print("2.删除学生")
    print("3.修改学生")
    print("4.查询学生")
    print("5.显示学生")
    print("6.退出")

# 添加学生
def add_student():
    # 接收用户输入的学生信息
    name = input("请输入学生的姓名")
    age = input("请输入学生的年龄")
    sex = input("请输入学生的性别")
    # 把参数封装到字典中
    student_dict = {}
    # 添加键值对
    student_dict["name"] = name
    student_dict["age"] = age
    student_dict["sex"] = sex
    #添加到学生列表里面，因为student_list是可变类型，添加数据不会对内存地址进行改变，不用添加global
    student_list.append(student_dict)

# 删除学生
def remove_student():
    # 接收用户输入的学生的序号
    num = input("请输入要删除学生的序号：")
    # 根据序号获取下表
    index = int(num) - 1
    # 控制下表范围，防止下表越界
    if index >= 0 and index < len(student_list):
        # 根据下表删除学生信息
        del student_list[index]
    else:
        print("请输入合法的序号")

# 修改学生信息
def modify_student():
    # 接收用户输入的学生序号
    num = input("请输入要修改学生的序号：")
    # 根据序号获取下标
    index = int(num) - 1
    # 控制下标的范围，防止越界
    if index >= 0 and index < len(student_list):
        # 根据下表获取学生的信息
        student_dict  = student_list[index]
        # 获取修改的信息
        new_name = input("请输入修改后的名字：")
        new_age = input("请输入修改后的年龄：")
        new_sex = input("请输入修改后的性别：")
        # 修改键值对信息
        student_dict["name"] = new_name
        student_dict["age"] = new_age
        student_dict["sex"] = new_sex

    else:
        print("请输入合法的数字")

# 查询学生信息
def query_student():
    # 获取用户输入的信息
    name = input("请输入要查询学生的信息：")
    for index, student_dict in  enumerate(student_list):
        if student_dict["name"] == name:
            print("找到了，信息如下：")
            print("序号：%d ， 姓名：%s， 年龄：%s， 性别：%s" % (index+1, student_dict["name"],student_dict["age"],student_dict["sex"]))
            # 找到了就需要在往后面循环进行判断
            break
        else:
            print("没有这个人的信息")

# 显示所有学生信息
def show_student_list():
    for index, student_dict in enumerate(student_list):
        print("序号：%d ， 姓名：%s， 年龄：%s， 性别：%s" % (index+1, student_dict["name"],student_dict["age"],student_dict["sex"]))

# 程序入口函数
def run():
    # 循环接收用户输入的指令
    while True:
        # 显示功能菜单
        show_menu()
        # 接收用户输入的指令
        menu_option = input("请输入功能选项:1-添加，2-删除，3-修改，4-查询，5-显示，6-退出")
        if menu_option == "1":
            # 输入1添加学生信息
            add_student()
        elif menu_option == "2":
            # 输入2删除学生信息
            remove_student()
        elif menu_option == "3":
            # 输入3修改学生信息
            modify_student()
        elif menu_option == "4":
            # 输入4查询学生信息
            query_student()
        elif menu_option == "5":
            # 输入5显示所有学生信息
            show_student_list()
        elif menu_option == "6":
            # 输入6退出
            break
        else:
            # 输入错误给出提示，重新输入
            print("请输入正确的功能选项")

#执行程序的入口函数
run()
