"""
1.面向对象和面向过程的区别
# 面向对象： 程序员(开发人员)面向的是功能对象， 不关心具体功能的实现步骤， 只关心对象是否具有我们需要的功能
# 面向对象的开发类似于： 程序员->功能对象.某个功能()

# 面向过程: 程序员面向的是功能实现的步骤，每一个步骤都需要程序员自己设计及开发，可以把实现的步骤封装到功能函数
# 面向过程的开发类似于： 程序员->功能函数

# 类： 事或者物的分类
# 对象： 具体到某一个事或者物就是对象
# 提示： 先有类然后通过类创建对应的对象
"""

"""
2.先定义类,然后通过类才能创建对象
class 类名:
    方法列表
"""
#定义类的关键字是class
#类的构成:1.类名 2.属性(特征) 4.方法(行为)
class Student:
    # 属性(类属性和对象(实例)属性)
    # 方法
    # self： 表示当前对象， 调用show_info方法的对象
    # self: 这个参数不需要我们自己去传参，系统帮我们去做
    # self参数名可以是其它的名字，但是一般情况下都是用self
    def show_info(self):
        print("大家好,我叫宋雨希,今年25岁")
#创建对象 :对象名 = 类名()
yuxi = Student()
#通过对象调用功能函数
yuxi.show_info()
#提示,类可以创建多个对象
#demo:定义老师类
class Teacher:
    # 定义方法
    def teach(self):
        print("正在授课中....")
    # 定义自我介绍的方法
    def show_info(self):
        print(self)
        print("我叫: %s 年龄: %d 性别:%s" % (self.name, self.age, self.sex))

# 创建对象
teacher = Teacher()
print(teacher)
# 给老师对象添加对象属性
teacher.name = "张老师"
teacher.age = 30
teacher.sex = "女"
# 获取对象属性-> 前提是对象已经存在了这些属性才能获取
# print(teacher.name, teacher.age, teacher.sex)
teacher.show_info()

# 创建对象
teacher1 = Teacher()
print(teacher1)
# 给老师对象添加对象属性
teacher1.name = "李老师"
teacher1.age = 30
teacher1.sex = "女"
# 获取对象属性-> 前提是对象已经存在了这些属性才能获取
# print(teacher.name, teacher.age, teacher.sex)
teacher1.show_info()

"""
3.新式类和旧式类
"""
# _*_ coding:utf-8 _*_
# 定义新式类
# object是所有类的根类
class Teacher(object):
    pass

# 定义旧式类
class Student:
    pass

# 总结： 在python3 里面旧式类默认继承object类， 在python2里面旧式类没有父类
# __bases__: 表示继承那个父类
print(Teacher.__bases__)
print(Student.__bases__)
# 建议： 为了兼容python2 我们以后定义可以选择使用新式类， 提示： 如果在python2里面没有继承object那么某些特殊功能无法实现

"""
4.init构造方法
def 类名:
    #初始化函数，用来完成一些默认的设定
    def __init__():
        pass

__init__()方法，在创建一个对象时默认被调用，不需要手动调用
__init__(self)中，默认有1个参数名字为self，如果在创建对象时传递了2个实参，那么__init__(self)中除了self作为第一个形参外还需要2个形参，例如__init__(self,x,y)
__init__(self)中的self参数，不需要开发者传递，python解释器会自动把当前的对象引用传递进去
"""
# init构造方法的作用: 给对象添加属性及对属性进行初始化
# 魔法方法： 以__开头及以__结尾的方法叫魔法方法，当程序想要完成某些特殊操作的时候程序自动调用对应的魔法方法
class Student(object):
    def __init__(self):
        self.name = "宋雨希"
        self.age = 25
        self.sex = "女"

    def show_info(self):
        print(self.name, self.age, self.sex)

#创建对象
student = Student()
student.show_info()

#init构造方法定义参数
class Student(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def show_info(self):
        print(self.name, self.age, self.sex)

# 创建对象
student = Student("张三", 25, "男")
student1 = Student("李四", 26, "女")
stusent2 = Student(name="王五", sex="女", age=27)
student.show_info()
student1.show_info()
stusent2.show_info()

"""
5.魔法方法str:当打印某个对象的时候,想要显示对象的描述信息的时候会自动调用str方法
"""
class Student(object):
    # 提供构造方法给对象添加数据及进行初始化
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 打印对象的时候显示对象的描述信息
    def __str__(self):
        return "我叫:%s 年龄:%d" % (self.name, self.age)
# 创建对象
student = Student("张三", 20)
#当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
print(student)

"""
6.魔法方法del:1.当程序退出后,程序里面所有的对象都会销毁
              2. 当前某个对象没有人使用的时候该对象也会销毁
              当有1个变量保存了对象的引用时，此对象的引用计数就会加1

当使用del删除变量指向的对象时，如果对象的引用计数不是1，比如3，
那么此时只会让这个引用计数减1，即变为2，当再次调用del时，变为1，如果再调用1次del，此时会真的把对象进行删除
"""
import time
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 显示对象的描述信息
    def __str__(self):
        return "名字是:%s, 年龄是:%d" % (self.name, self.age)
    # 对象销毁的时候会调用下面的方法
    def __del__(self):
        print("对象销毁啦")

# 创建对象
person = Person("小明", 20)
print(person)
person1 = person
# 删除对象-> 删除变量保存的内存地址，然后在删除变量名
del person
del person1
# 对象是否销毁是通过引用计数来控制,引用计数就是内存地址使用个数，引用计数为0表示对象释放,否则不释放
# 让程序等待5秒钟后再继续往下执行对应的代码
time.sleep(5)
print("程序退出啦")

"""
7.继承:子类继承父类,可以拥有父类的方法或者属性
"""
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 开酒店
    def open_hotel(self):
        print("开酒店")
# 对应当前代码来说 Student 是子类（派生类）， Person 是父类(基类)
class Student(Person):
    # 提供了构造方法
    def __init__(self, subject):
        # 默认不会调用父类的构造方法，可以手动调用
        super(Student, self).__init__("张三", 18)
        self.subject = subject
    # 默认都是调用自己的，如果自己没有可以使用父类的
    def open_hotel(self):
        print("Student开酒店")
# 创建学生对象
# 提示： 子类不提供构造方法或者其他方法都是可以使用父类的，但是子提供了构造方法和其它方法是先使用自己的
student = Student("python")
print(student.name, student.age)
student.open_hotel()

"""
8.单继承:子类只继承一个父类,可以拥有父类的属性和方法
"""
# 定义动物类
class Animal(object):
    # 吃的方法
    def eat(self):
        print("吃东西")
# 定义狗类
class Dog(Animal):
    pass
dog = Dog()
dog.eat()

#注意点
class Animal(object):
    def __init__(self, name='动物', color='白色'):
        self.__name = name
        self.color = color

    def __test(self):
        print(self.__name)
        print(self.color)

    def test(self):
        print(self.__name)
        print(self.color)

class Dog(Animal):
    def dogTest1(self):
        #print(self.__name) #不能访问到父类的私有属性
        print(self.color)

    def dogTest2(self):
        #self.__test() #不能访问父类中的私有方法
        self.test()

A = Animal()
#print(A.__name) #程序出现异常，不能访问私有属性
print(A.color)
#A.__test() #程序出现异常，不能访问私有方法
A.test()

print("------分割线-----")

D = Dog(name = "小花狗", color = "黄色")
D.dogTest1()
D.dogTest2()

#总结
# 私有的属性，不能通过对象直接访问，但是可以通过方法访问
# 私有的方法，不能通过对象直接访问
# 私有的属性、方法，不会被子类继承，也不能被访问
# 一般情况下，私有的属性、方法都是不对外公布的，往往用来做内部的事情，起到安全的作用

"""
9.多继承
"""
# 定义亲爸爸
class Father(object):
    def open_hotel(self):
        print("开酒店")
    def open_flower_shop(self):
        print("Father 开花店")
# 定义干爸爸
class GodFather(object):
    def open_flower_shop(self):
        print("GodFather 开花店")
# 定义儿子类
class Son(Father, GodFather):
    pass
# 创建儿子对象
xiao_run = Son()
xiao_run.open_hotel()
xiao_run.open_flower_shop()
# 查看类继承的顺序
print(Son.mro())
# 提示： 多个父类有相同的方法，使用方法调用的顺序， 就是按照类继承顺序查找
# 总结： 类继承顺序， 方法调用按照这个顺序进行对方法的查找，
# 如果在某个对象里面找到了那么久不会往后继续查找了，否则再继续查找，如果最终没有找到直接崩溃
# 默认是使用的第一个父类里面的方法的


"""
10.子类重写父类的方法
"""
class Person(object):
    def run(self):
        print("跑起来")

class Student(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 重写： 子类继承父类在拥有父类方法的基础上继续重写， 重写的目的是： 父类的方法无法满足我们的需要
    # 重写后按照自己的需求重写开发
    def run(self):
        print("%s 跑起来" % self.name)


student = Student("张三", 20)
student.run()

"""
11.子类调用父类的同名方法
"""
class Father(object):
    def open_hotel(self):
        print("Father: ",self)
        print("开酒店")

class Son(Father):
    # 重写父类的方法
    def open_hotel(self):
        # 如果外面的函数名和你调用函数不同这样做是可以的
        # self.open_hotel()
        # 使用父类去调用父类的方法
        print("Son:", self)
        Father.open_hotel(self)
        # 注意点： 对象调用方法不需要传入参数，类调用方法需要传入self参数
        print("开五星级酒店")

son = Son()
son.open_hotel()

"""
12.多层继承
"""
# 多层继承： 多个层次的继承关系
# 猿类
class Monkey(object):
    def run(self):
        print("跑起来")

class Person(Monkey):
    def eat(self):
        print("吃东西")

class Student(Person):
    def study(self):
        # 1. 使用父类或者爷爷类可以调用对应的方法
        # Monkey.run(self)
        # Person.eat(self)
        # 2. 使用self调用父类或者爷爷类可以调用对应的方法
        # 注意点: 当使用self调用的方法和当前方法不同可以使用self，如果相同不能使用self可以选择使用类调用
        self.run()
        self.eat()
        print("学习")
# 创建学生对象
student = Student()
student.study()
# student.eat()
# student.run()

"""
13.super调用父类方法
"""
class Person(object):
    def run(self):
        print("跑起来")

class Student(Person):

    def __init__(self, name):
        self.name = name

    # 重写父类的方法
    def run(self):
        # 使用self不要调用同名方法
        # self.run()
        # 使用类名去调用
        # Person.run(self)
        # super(): 表示创建了一个父类对象
        # super().run()  => super(Student, self).run()

        # 通过Student创建父类对象，调用父类对象的方法
        super(Student, self).run()
        # super调用也会遵循mro，类继承顺序的规则
        # print(Student.mro())
        # super(Person, self).run()
        print("%s 跑起来" % self.name)

student = Student("张三")
student.run()

"""
14.super的总结
"""

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    # 子提供构造方法默认不会调用父类的构造方法
    def __init__(self, name, age, subject):
        self.subject = subject
        # 手动调用父类的构造方法
        super(Student, self).__init__(name, age)
        # 建议： 以后在构造方法里面建议大家调用父类的构造方法，因为如果子类提供了构造方法默认不会调用父类的构造方法
# 对象属性如果子类没有构造方法，可以继承父类的对象数据， 如果子类提供了构造方法，默认不会调用父类的构造方法也就是说父类的属性不会继承
# 想要使用属性需要手动调用父类的构造方法才可以给对象添加属性

# 子类提供构造方法
student = Student("zs", 20, "python")
print(student.name, student.age, student.subject)

# 如果子类没有提供构造方法，那么可以使用父类的构造方法创建对象
# student = Student("李四", 20)
#
# print(student.name, student.age)


















































