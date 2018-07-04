# 1.函数的介绍:程序员自己提供的具有某些功能的代码块,可以提高代码的复用性和编写代码的效率,降低冗余
# 打印佛祖镇楼
def show_info():
    print("                            _ooOoo_  ")
    print("                           o8888888o  ")
    print("                           88  .  88  ")
    print("                           (| -_- |)  ")
    print("                            O\\ = /O  ")
    print("                        ____/`---'\\____  ")
    print("                      .   ' \\| |// `.  ")
    print("                       / \\||| : |||// \\  ")
    print("                     / _||||| -:- |||||- \\  ")
    print("                       | | \\\\\\ - /// | |  ")
    print("                     | \\_| ''\\---/'' | |  ")
    print("                      \\ .-\\__ `-` ___/-. /  ")
    print("                   ___`. .' /--.--\\ `. . __  ")
    print("                ."" '< `.___\\_<|>_/___.' >'"".  ")
    print("               | | : `- \\`.;`\\ _ /`;.`/ - ` : | |  ")
    print("                 \\ \\ `-. \\_ __\\ /__ _/ .-` / /  ")
    print("         ======`-.____`-.___\\_____/___.-`____.-'======  ")
    print("                            `=---='  ")
    print("  ")
    print("         .............................................  ")
    print("                  佛祖镇楼                  BUG辟易  ")
    print("          佛曰:  ")
    print("                  写字楼里写字间，写字间里程序员；  ")
    print("                  程序人员写程序，又拿程序换酒钱。  ")
    print("                  酒醒只在网上坐，酒醉还来网下眠；  ")
    print("                  酒醉酒醒日复日，网上网下年复年。  ")
    print("                  但愿老死电脑间，不愿鞠躬老板前；  ")
    print("                  奔驰宝马贵者趣，公交自行程序员。  ")
    print("                  别人笑我忒疯癫，我笑自己命太贱；  ")
    print("                  不见满街漂亮妹，哪个归得程序员？")

menu_option = input("请输入功能选项:0, 1:")
if menu_option == "0":
    show_info()
elif menu_option == "1":
    show_info()


#2.函数的定义和调用
# 定义函数的格式
# def 函数名(参数列表，...):
#     # 函数实现代码

# 定义显示打印信息函数
def show_info():
    print("这个社会是一个和谐的社会")
# 调用函数
show_info()

#3.函数的文档说明
# 函数文档说明
def sum_num(num1, num2):
    """
    完成两数相加的功能
    """
    result = num1 + num2
    print(result)
# 查看函数的文档说明,使用help
help(sum_num)

#4.函数的参数
# 完成两数相加的功能函数
def sum_num(num1, num2):  # 定义的带有参数的函数，参数放到小括号里面
    print("num1:", num1 , "num2:", num2)
    result = num1 + num2
    print(result)
# 调用函数 =》 函数名(参数,xx)
sum_num(1, 2)

#5.函数的返回值
#定义由两个参数和一个返回值的函数
def sum_num(num1,num2):
    print(num1, num2)
    result = num1+num2
    print(result)
    return result
#调用函数的时候,如果函数由返回值,那么会给调用方,调用方想使用的话需要用一个变量保存
result = sum_num(5,6)
print(result)

# 不处理返回值，不会报错，代码可以正常运行， 一般要处理返回值
sum_num(2, 4)

def show_info():
    print("惺惺惜惺惺")
    # 可以return None， 或者 不加return操作返回也是None
    return None

result = show_info()
print(result)

#6.函数的四种类型
# 1. 无参数无返回值
# 2. 无参数有返回值
# 3. 有参数无返回值
# 4. 有参数有返回值
# 总结: 函数有没有参数看定义的小括号里面有没有参数名，函数有没有返回值，看函数里面有没有return 返回值

# 1. 无参数无返回值
def show_info():
    print("社会我彬哥，人狠话不多!")
# 2. 无参数有返回值
def show_desc():
    return "你好， python!"
# 3. 有参数无返回值
def show_student_info(name, age, sex):
    print(name, age, sex)
# 4. 有参数有返回值
def show_dog_info(nick_name, age):
    msg = "狗的昵称:%s 狗龄:%d岁" % (nick_name, age)
    return msg
# 调用的是无参数无返回值的函数
show_info()
# 调用的是无参数有返回值的函数
result = show_desc()
print(result)
# 有参数无返回值
# 注意参数需要安装一定顺序去传参
show_student_info("蔡广义", 23, "男")
# 有参数有返回值函数
msg = show_dog_info("贝贝", 1)
print(msg)


#7. 函数的嵌套调用:在函数里面调用其他函数的操作叫做函数的嵌套调用
def print_info1():
    print("开始执行 print_info1")
    print("好好学习，天天向上")
    print("结束执行 print_info1")

def print_info2():
    print("开始执行 print_info2")
    # 调用函数1，把函数1里面的代码执行完成以后再继续执行下面的代码
    # 在函数里面又调用了其它函数就是函数的嵌套调用
    print_info1()
    print("机会是留给有准备的人的")
    print("结束执行 print_info2")

# 调用函数2
print_info2()

#8.函数的嵌套:在函数里面再定义函数
def show_info():
    # 在函数里面在定义函数，那么这个函数也称为子函数
    def print_num():
        print("哈哈")
    # 调用嵌套函数，或者说调用子函数
    print_num()
# 调用函数
show_info()

#需求:使用冰箱的步骤:打开冰箱,放入吃的,关闭冰箱
def use_bx(eat):
    #1.打开冰箱
    def open_bx():
        print("打开冰箱")
    #2.放入吃的
    def input_eat(eat):
        print("放入%s" % eat)
    #3.关闭冰箱
    def close_bx():
        print("关闭冰箱")
    open_bx()
    input_eat(eat)
    close_bx()

use_bx("苹果")