# 模块的命名规则: 模块的命名规则和变量名的命名规则一样，不能以数字开头， 是由字母、数字、下划线组成

# 对应外界使用from 模块名 import * 导入的时候不让其把所有的功能代码都导入，可以指定导入的功能代码
# 提示: 指定__all__功能代码只对from 模块名 import * 起作用，其它方式导入都没有问题可以正常使用
__all__ = ["calc_num"]

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super(Person, self).__init__()

    def run(self):
        print("%s跑起来" % self.name)


def calc_num(num1, num2):
    print("first_module")
    return num1 + num2


# 全局变量
num = 10

# person = Person("张三", 20)
# person.run()