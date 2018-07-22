"""
1.多继承使用super的注意点
"""

class A(object):
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super(B, self).__init__()

class C(object):
    def __init__(self):
        print("C")

class D(C):
    def __init__(self):
        print("D")

class E(B, D):
    def __init__(self):
        print("E")
        # 如果子类提供了构造方法，那么默认不会自己调用父类的构造方法，如果想要调用父类的构造方法需要手动调用
        # super(E, self).__init__()
        super(E, self).__init__()

# 以后不太清楚可以查看类继承属性，super具体使用哪个父类对象取决于这个类继承顺序
print(E.mro())
e = E()
# # 总结： 多继承的调用顺序的特点是: 先左再右，最后是object类

# class A(object):
#     def __init__(self):
#         print("A")
#         # super(A, self).__init__()
#         D.__init__(self)
#
# class B(A):
#     def __init__(self):
#         print("B")
#         # super(B, self).__init__()
#         A.__init__(self)
#
# # class C(object):
#     def __init__(self):
#         print("C")
#         # super(C, self).__init__()
#         object.__init__(self)
# class D(C):
#     def __init__(self):
#         print("D")
#         # super(D, self).__init__()
#         C.__init__(self)
# class E(B, D):
#     def __init__(self):
#         print("E")
#         # 如果子类提供了构造方法，那么默认不会自己调用父类的构造方法，如果想要调用父类的构造方法需要手动调用
#         # super(E, self).__init__()
#         B.__init__(self)

# 以后不太清楚可以查看类继承属性，super具体使用哪个父类对象取决于这个类继承顺序
# print(E.mro())
# e = E()

# 总结： 多继承的调用顺序的特点是: 先左再右，最后是object类

"""
2.面向对象的三大特征
"""
# 1. 封装： 把属性和方法放到类里面，使用方法封装功能实现的具体步骤，通过对象访问属性和方法，当然还可以同访问权限控制访问属性和方法
# 2. 继承： 子类需要使用父类的功能， 当然如果父类的方法不能满足子类的需要还可以重写
# 3. 多态： 同一个方法不同对象调用会出现不同的表现形式

"""
3.私有属性和私有方法
"""


# 私有属性和私有方法都是在属性名或者方法名前面加上两个下划线'__'
class Person(object):
    def __init__(self):
        # 默认都是公开的属性
        self.name = "李四"
        # 添加私有属性，在外界不能直接访问，只能在类内部使用
        self.__age = 18

    # 默认定义公开方法
    def show_info(self):
        # 私有属性可以在类内部使用，在外面无法调用
        print(self.name, self.__age)
        # 在类内部使用私有方法
        result = self.__show_money()
        print(result)

    # 定义私有方法
    def __show_money(self):
        return "100万"

# 创建对象
person = Person()
# 调用公开的方法
person.show_info()
# 在外界调用私有方法是不可以的
# person.__show_money()
# print(person.name, person.__age)

# 扩展： 私有属性和方法只是把属性或者方法名进行了伪装，改成了其它名字而已

# 查看对象属性
print(person.__dict__)
# 非常规操作
print(person._Person__age)
# 查看对象的属性和方法
print(dir(person))

# 总结: __dict 可以使用对象或者类查看对象或者类的属性
# dir：可以查看对象和类的方法及属性

"""
4.子类继承父类,无法使用父类的私有属性和方法
"""
class Person(object):
    def __init__(self):
        # 默认都是公开的属性
        self.name = "李四"
        # 添加私有属性，在外界不能直接访问，只能在类内部使用
        self.__age = 18

    # 默认定义公开方法
    def show_info(self):
        # 私有属性可以在类内部使用，在外面无法调用
        print(self.name, self.__age)
        # 在类内部使用私有方法
        result = self.__show_money()
        print(result)

    # 定义私有方法
    def __show_money(self):
        return "100万"

# 学生类
class Student(Person):
    def __init__(self):
        super(Student, self).__init__()

        # 查看当前对象的属性及方法
        # result = dir(self)
        # print(result)

        # 访问父类的私有属性
        # print(self.__age)
        print(self._Person__age)
        # result = self.__show_money()
        result = self._Person__show_money()
        print(result)

# 创建学生对象
student = Student()

# 错误演示
# 访问私有属性
# print(student.__age)
# 访问私有方法
# student.__show_money()

"""
5.修改私有属性
"""
class Person(object):
    def __init__(self):
        # 私有属性
        self.__age = 18

    # 修改私有属性
    def set_age(self, age):
        # 在类内部可以对私有属性进行修改
        self.__age = age

    # 获取私有属性的值
    def get_age(self):
        return self.__age

person = Person()
# print(person.__dict__)
# # 本意是想要直接在外界修改私有属性
# # 注意点： 不是修改了私有属性是添加了一个属性，名字叫做'__age'
# person.__age = 20
# print(person.__dict__)
# print(person.__age)

# 使用共有方法修改私有属性
print(person.__dict__)
person.set_age(20)
result = person.get_age()
print(person.__dict__)
print(result)
# 非常规操作,直接方法伪装后的属性
# print(person.__dict__)
# person._Person__age = 20
# print(person._Person__age)
# print(person.__dict__)

"""
6.多态:不关心对象的类型,只关心对象是否存在指定功能,不同对象调用会有不同的表现形式
"""
# 多态：不关心对象的类型，只关心对象是否存在指定功能，不同对象调用会有不同的表现形式
class Bird(object):
    def fly(self):
        print("鸟飞起来了")

# 天鹅类
class Swan(Bird):
    def fly(self):
        print("天鹅飞起来了")
# 鸭子类
class Duck(Bird):
    def fly(self):
        print("鸭子沿着地面飞起来了")
class Plane(object):
    def fly(self):
        print("飞机飞起来了")
# 创建具体对象
bird = Bird()
swan = Swan()
duck = Duck()
plane = Plane()
# 根据指定对象显示飞的功能
def fly(obj):
    # 注意点：在其他语言里面是需要关心类型的, 只能传指定类型的对象获取其子类的对象，比如： java， c#
    # 在python里面多态：不关心类型只关心对象是否有该功能，像这样的操作就是多态的表现实现
    obj.fly()
# 调用函数
fly(plane)
fly(swan)
fly(duck)
fly(bird)

"""
7.类属性和实例(对象)属性
"""
class Person(object):
    #定义类属性:在类里面方法外面定义的属性就是类属性
    contry = "中国"
    def __init__(self, name, age):
        #实例属性也叫对象属性
        self.name = name
        self.age = age
#访问类属性
print(Person.contry)
#对象可以访问类属性
person = Person("宋雨希", 25)
print(person.contry)
print(person.name)
print(person.age)

#使用类修改类属性
Person.contry = "美国"
print(Person.contry)

#注意点:对象不能修改类属性,下面的操作是给对象添加一个对象属性,只不过名字和类属性相同而已
print(person.__dict__)
person.contry = "日本"
#访问自己添加的对象属性
print(person.contry)
print(person.__dict__)

#对象属性只能对象访问,那么修改也只能对象来修改
person.name = "李四"
person.age = 15
#访问对象属性
print(person.name, person.age)

#类不能访问对象属性
#总结:对象属性的操作使用对象来完成,类属性的操作使用类去完成

#扩展
class Student(Person):
    def __init__(self):
        self.subject = "python"

student = Student()
print(student.subject, student.contry)
#总结:类属性是可以继承下来的,但是对象属性如果子类提供了构造方法则不调用父类的构造方法,
#默认是部继承的,除非调用父类的构造方法

"""
8.类方法和静态方法
"""
class Person(object):
    # 类属性
    contry = "中国"
    def __init__(self):
        #实例属性,也叫对象属性
        self.name = "zhangsan"
        self.age = 20
#demo:
class Person(object):
    # 类属性
    contry = "中国"
    def __init__(self):
        self.name = "zhangsan"
        self.age = 20

    # 定义类方法的目的就是通过类方法可以访问和修改类属性
    @classmethod
    def set_contry(cls, contry):
        cls.contry = contry
        # 注意点：在类方里面不能修改对象属性, 除非传入指定的对象和修改的值

    @classmethod
    def get_contry(cls):
        return cls.contry

    # 定义类方法
    @classmethod # 使用classmethod关键字修改的方法就是类方法，通俗理解可以使用类去调用，注意点： 对象也可以调用
    def show_info(cls):
        # cls:表示当前类, 提示： cls参数名还可以改天其它的，但是一般都是默认使用cls
        print(cls)
        print("哈哈，我是类方法")

    # 对象方法可以访问和修改对象属性
    def set_name(self, name):
        self.name = name
        # 对象方法可以修改类属性
        # 1. 直接使用类修改类属性
        # Person.contry = "俄罗斯"
        # 2. 通过对象获取指定的类
        self.__class__.contry = "俄罗斯"

    def get_name(self):
        return self.name

    # 定义对象(实例)方法
    def show_money(self):
        print("show_money:", self)
        return "30万"

    # 静态方法： 不需要对象方法里面的self参数还有不需要类方法里面cls参数可以直接定义成静态方法
    # 通俗理解可以把静态方法想成把函数放到类里面
    @staticmethod
    def show_msg():
        print("我是静态方法")

    @staticmethod
    def show_address(address):
        print("我是静态方法")
        print(address)
        # 注意点： 静态方法不能使用self对象，不能修改对象属性
        # 可以使用类访问和修改类属性
        Person.contry = "美国"

# 通过类去调用类方法
Person.show_info()
# 创建对象调用类方法
person = Person()
# 通过对象获取对象的类
result = person.__class__
print(result)
person.show_info()
# 使用对象调用对象方法
result = person.show_money()
print(result)
# 类也可以调用对象方法，但是需要传入对象参数
# 如果使用类调用对象方法需要把对象提前准备好传入过去
print("person:", person)
Person.show_money(person)
# 静态方法可以使用类和对象调用
Person.show_msg()
person.show_msg()
person.show_address("北京")
print(Person.contry)
Person.set_contry("日本")
print(Person.get_contry())
person.set_name("李四")
print(person.get_name())
print(Person.contry)
# 总结： 类方法：使用@classmethod关键字修改的方法就是类方法，类方法只能修改类属性
# 对象方法： 在方法的参数里面如果有self对象参数那么可以认为是对象方法，对象方法可以修改对象属性和类属性
# 静态方法： 使用staticmethod关键字修饰，在方法的参数里面不需要使用self和cls参数就可以称为是静态方法，静态方法可以修改类属性


"""
9.new方法的使用
"""
# 创建对象背后做了两件事件，1. 先通过new方法创建对象，
# 2. 然后通过对象调用init方法给对象添加属性及初始化
class Person(object):
    # 创建对象调用new方法
    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        print(cls)
        # 创建对象的操作需要调用父类的方法
        # 使用父类的new方法帮我们创建对象
        return object.__new__(cls)

    # 给对象添加属性及对属性进行初始化
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 创建对象
# person = Person("张三", 20)
person = Person()
print(person.name, person.age)

























