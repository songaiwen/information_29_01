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

# 如果在开发程序时，需要某块代码多次，但是为了提高编写的效率以及代码的重用，
# 所以把具有独立功能的代码块组织为一个小模块，这就是函数

# menu_option = input("请输入功能选项:0, 1:")
# if menu_option == "0":
#     show_info()
# elif menu_option == "1":
#     show_info()


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
# 定义时小括号中的参数，用来接收参数用的，称为 “形参”
# 调用时小括号中的参数，用来传递给函数用的，称为 “实参”
# 完成两数相加的功能函数
def sum_num(num1, num2):  # 定义的带有参数的函数，参数放到小括号里面
    print("num1:", num1 , "num2:", num2)
    result = num1 + num2
    print(result)
# 调用函数 =》 函数名(参数,xx)
sum_num(1, 2)

#需求:打印名片
def printCard(name, tel, money):#形参
    #注意:
    #1. 如果函数定义了3个形参,那么意味着将来 不管谁调用这个函数 都要给这个函数传递3个参数
    #2. 参数在传递的时候是 个数要相同,并且先后顺序也相同,即"老赵"给name  "10010"给tel....
    #3. 如果一个函数有参数的话,那么这个函数往往会更通用,因为传递的数据可以不一样但是依然可以做事情
    if money<100:
        print("钱不够,请缴费")
    else:
        #name = "老李"
        #tel = "10086"
        print("="*30)
        print("姓名:%s"%name)
        print("手机号:%s"%tel)
        print("="*30)
printCard("老赵", "10010", 10)#实参

#需求:计算1到某个数值的偶数和
def sum_1_to_num(num):
    i=1
    sumResult = 0
    while i<=num:
        if i%2==0:
            sumResult += i
        i+=1
    print(sumResult)
sum_1_to_num(6)

#5.函数的返回值:想要在函数中把结果返回给调用者，需要在函数中使用return
#定义有两个参数和一个返回值的函数
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

#需求:用函数求两个数的平均值
def sum_2_nums(a, b):
    # 定义了2个形参用来接受 调用时传递过来的数值
    result = a + b
    # print(result)
    # 如果一个函数中有return,那么也就意味着 return后面的值 是需要返回给调用者的
    return result

def average_2_nums(num):
    result = num / 2
    # print(result)
    return result
# 调用了一个函数,如果这个函数需要2个参数,那么就给它传递2个参数,注意顺序是一一对应的
# 如果调用的函数中有return,那么也就意味着这个函数有一个结果会返回到这
# 为了能够保存返回过来的这个结果,需要在调用函数前用一个变量来保存
numResult = sum_2_nums(100, 123)
print(numResult)

# 在调用一个函数的时候,传递的参数不仅是100那样的数值,还可以是一个变量的,此时意味着:
# 把这个变量numResult中的数值传递给average_2_nums函数中的形参num
result = average_2_nums(numResult)
print(result)

#6.函数的四种类型
# 1. 无参数无返回值:不能接收参数，也没有返回值，一般情况下，打印提示灯类似的功能，使用这类的函数
"""
def 函数名():
    语句
"""

# 2. 无参数有返回值:不能接收参数，但是可以返回某个数据，一般情况下，像采集数据，用此类函数
"""
 def 函数名():
        语句
        return 需要返回的数值
"""
# 3. 有参数无返回值:能接收参数，但不可以返回数据，一般情况下，对某些变量设置数据而不需结果时，用此类函数
"""
    def 函数名(形参列表):
        语句
"""
# 4. 有参数有返回值:不仅能接收参数，还可以返回某个数据，一般情况下，像数据处理并需要结果的应用，用此类函数
"""
 def 函数名(形参列表):
        语句
        return 需要返回的数值
"""
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
#需求:计算两个数的平均数
def sum_2_nums(a,b):
    result = a+b
    return result

def average_2_nums(A, B):
    result = sum_2_nums(A, B) / 2
    #print(result)
    return result
result = average_2_nums(100,123)
print(result)



#9.函数的应用
#需求:用函数求三个数的和
def sum_num(num1,num2,num3):
    result = num1 + num2 + num3
    return result
# print(sum_num(1,2,3))
#需求:用函数求三个数的平均值
def avg_num(num1,num2,num3):
    result = sum_num(num1,num2,num3)
    result = result / 3
    return result
print(avg_num(10,20,30))


#10.局部变量:在函数里面使用的变量就叫做局部变量,在函数外面不能使用
def print_num():
    #在函数里面定义的局部变量
    #定义局部变量的作用是在函数里面临时保存一些数据,函数调用完成以后局部变量会被释放
    #而return返回的值,外界使用完成以后才会释放
    num = 10
    print(num)
print_num()


#11.全局变量:定义在函数外面,可以被不同函数使用的变量就是全局变量
num = 20
def show_info():
    #这里面的变量是局部变量,只不过是局部变量的名字和全局变量的名字相同
    # num = 10
    # # 特点: 在函数里面使用的变量先从局部变量查找，如果找到了那么使用局部变量，
    # # 没有找到再去全局变量去找，找到了使用全局变量， 在全局变量也没有找崩溃
    # # 总结：在函数里面使用变量是有一个就近原则
    # print(num)

    #想要修改全局变量可以用global生命
    #如果全局变量的名字和局部变量的名字相同，那么使用的是局部变量的，小技巧强龙不压地头蛇
    global num
    num = 30
    print(num)
    # 在函数中不使用global声明全局变量时不能修改全局变量的本质是不能修改全局变量的指向，即不能将全局变量指向新的数据。
    # 对于不可变类型的全局变量来说，因其指向的数据不能修改，所以不使用global时无法修改全局变量。
    # 对于可变类型的全局变量来说，因其指向的数据可以修改，所以不使用global时也可修改全局变量。

show_info()


#12多函数使用的基本流程
#1.全局变量:不同函数使用全局变量可以完成数据的共享
# 定义全局变量
num = 1
def show_num():
    global num
    num = 3
    print(num)

def show_num1():
    print(num)

show_num()
show_num1()

#2.函数的返回值,作为其他函数的参数
def return_value():
    return 50

#显示函数的参数的数据
def show_info(value):
    print("参数值为:", value)

result = return_value()
show_info(result)


#13.函数有多个返回值
"""
在函里面多个return语句语法上是没有问题,
但是代码执行到return语句以后,函数执行结束,会回到调用的地方,
return后面的语句不在执行了
"""
def return_more_value():
    print("我是中国人")
    # return [1,2]
    # return {"name":"songyuxi","age":20}
    # return (1,2)
    # return 3,4  #如果不想外界修改返回的数据可以使用元祖类型,想要修改可以使用字典或者列表
    return {6,7}

result = return_more_value()
print(result,type(result))


#14.缺省参数:可选参数,如果给参数传值,那么使用传入过来的值,否则使用默认值
#需求:计算两个数的和
#提示:缺省参数不能放到普通参数前面,缺省参数后面还可以使用缺省参数
#注意：带有默认值的参数一定要位于参数列表的最后面。
# 错误的写法
# def sum_num(num2=10, num1):
#     return num1 + num2

def sum_num(num1,num2=10):
    return  num1 + num2
print(sum_num(1,9))

#需求:显示学生信息的功能函数
def student_info(name,age):
    print("姓名:",name, "年龄:",age)
#使用位置参数调用函数,位置参数一定按着函数参数定义的顺序去传参
student_info("宋雨希",25)
#如果不按着顺序传参显示的信息就是错的
student_info(18,"宋佳赢")
#但是如果使用关键字参数调用函数时,根据函数的参数名设置参数值,可以打乱顺序
student_info(age = 20, name="songjiaying")


#15.不定长参数:不确定用户传入多少个参数,可能是0个也可能是1个或者多个
# 不定长参数分为:不定长位置参数,和不定长关键字参数
#*args:表示接受不定长位置参数
def sum_num(*args):
    #args:把位置参数封装到元祖里面,类型就是元祖
    print(args,type(args))
    result = 0
    #遍历元祖
    for value in args:
        result += value
    return result
result = sum_num(1,2,3,4)
print(result)
#**kwargs:表示可以接受不定长关键字参数
def show_info(**kwargs):
    #**kwargs:把关键字参数封装到字典里面,类型就是字典
    print(kwargs,type(kwargs))
    for key,value in kwargs.items():
        print(key,value)
    result = kwargs['a']
    print(result)
#按着关键字方式进行调用函数
show_info(a=1, b=2)
#总结:
# 加了星号（*）的变量args会存放所有未命名的变量参数，args为元组；
# 而加**的变量kwargs会存放命名参数，即形如key=value的参数， kwargs为字典。

#16.函数参数的高级用法
def show_info(name, age=18, *args):
    print(name, age, args)
#args是接受不定长位置参数的,所以这个只能按着位置方式进行传参
show_info("李四","男", 122)


def show_info(*args, name, age=18):
    print(name, age, args)
#*args如果放到普通参数前面,不能使用位置方式传参
#前面使用位置参数给不定长位置参数传参,后面使用关键字参数给name和age传参
show_info(1,3,10, name="wangwu", age=20)

#如果有其他参数,**kwargs必须放在参数的最后面
def show_info(name, age=18, *args, **kwargs):
    print(name,age,args,kwargs)
show_info("赵四",20,"男",100,a=1,b=2)

#如果由缺省参数,又不想给缺省参数传值,可以放到*args后面
def show_info(name, *args, age=23, **kwargs):
    print(name, age, args, kwargs)
show_info("刘能","男", a=1, b=2)

#常见用法
def show_info(name,*args, **kwargs):
    print(name,args,kwargs)
show_info("长脚", "男", 100, age=20, a=1, b=2)


#17.只按着关键字传参
# *,    后面的参数都是按着关键字方式进行传参
def show_info(*, name, age):
    print(name, age)
show_info(name="laozhao", age=28)

#18.函数高级补充
def show_info(*args, **kwargs):
    print(args, kwargs)
# show_info(1,2, a=2, b=5)
my_tuple = (5,6)
my_dict = {"name":"宋雨希", "age":28}

#my_tuple:把元祖拆分成对应的位置参数
#my_dict:把字典拆分成对应的关键字参数
show_info(*my_tuple, **my_dict)

#19.拆包:把集合中的每一个元素,拆分到不同变量进行保存
# 可以拆包的类型:字典,列表,元祖,集合,字符串
a, b = (1, 2)
print(a, b)
a, b = [3, 4]
print(a, b)
a, b = {"A", "B"} # set 集合
print(a, b)
a, b = "AB"
print(a, b)
a, b = {"name": "陈明", "age":20}.values()
print(a, b)
#拆包的操作
for key,value in {"name":"songyuxi", "age":18}.items():
    print(key, value)


#20,交换两个变量的值
num8 = 10
num9 = 20
#方法1:使用临时变量,完成两个变量值的交换
num6 = num8
num8 = num9
num9 = num6
print(num8, num9)
#方法2:可以给两个变量赋值
result1 = 1000
result2 = 2000
result1, result2 = result2, result1
print(result1,result2)


#21.函数的应用:数据在内存中的地址,也可以说是内存地址,引用就是内存地址
#引用:指向都说的是内存地址
a = 50
#我们之前都说变量a存储的数据是10, 因为变量是存储数据的容器
#严格意义应该是:变量是存储数据在内存中的地址,变量保存的是数据的内存地址
#通过id()可以查看变量保存的内存地址
result = id(a)
print(result, hex(result))
print(a) # 通过内存地址找内存中找到对应的数据，然后返回给用户

b = a  # b保存的是a存储的内存地址
result = id(b)
print(result, hex(result))
print(b)

a = 11
result = id(a)
print(a, b, hex(result))

# 创建列表
my_list = [1,2]
my_list1 = my_list

my_list_address = id(my_list)
my_list1_address = id(my_list1)
# 把10进制转成16进制
print(hex(my_list_address), hex(my_list1_address))


my_list.append(3)
my_list_address = id(my_list)
my_list1_address = id(my_list1)
# 把10进制转成16进制
print(hex(my_list_address), hex(my_list1_address))
print(my_list, my_list1)



































































