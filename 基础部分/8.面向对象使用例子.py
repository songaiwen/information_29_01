class Person(object):
    # 烤地瓜
    def roast(self, sweet_potato, time):
        # 烤的时间需要进行修改
        sweet_potato.roast_time += time
        if sweet_potato.roast_time > 8:
            # 修改烤的状态
            sweet_potato.roast_state = "糊了"
        elif sweet_potato.roast_time > 5:
            # 修改烤的状态
            sweet_potato.roast_state = "熟了"

        elif sweet_potato.roast_time > 3:
            # 修改烤的状态
            sweet_potato.roast_state = "半生不熟"
        else:
            # 修改烤的状态
            sweet_potato.roast_state = "生的"
    # 查看地瓜状态
    def show_info(self, sweet_potato):
        print(sweet_potato)
# 定义地瓜类
class SweetPotato(object):
    # 提供构造方法，给对象添加属性及设置初始值
    def __init__(self):
        # 烤的时间
        self.roast_time = 0
        # 烤的状态
        self.roast_state = "生的"
        # 佐料列表
        self.condiment_list = []

    # 烤地瓜  -》 提示：本质上应该把烤地瓜方法放到人类里面
    def roast(self, time):
        # 烤的时间需要进行修改
        self.roast_time += time
        if self.roast_time > 8:
            # 修改烤的状态
            self.roast_state = "糊了"
        elif self.roast_time > 5:
            # 修改烤的状态
            self.roast_state = "熟了"

        elif self.roast_time > 3:
            # 修改烤的状态
            self.roast_state = "半生不熟"
        else:
            # 修改烤的状态
            self.roast_state = "生的"
    # 添加佐料
    def add_condiment(self, condiment):
        self.condiment_list.append(condiment)

    # 显示对象的描述信息
    def __str__(self):
        if self.condiment_list:
            # 显示佐料信息
            # "熟了地瓜[老干妈，番茄酱]"
            # 1. 遍历佐料列表进行字符串拼接
            # 2. 使用字符串里面join把列表转成字符串
            print(self.condiment_list)
            result = ",".join(self.condiment_list)
            # print(result)

            return self.roast_state + "地瓜" + "[" + result + "]"
        else:
            return self.roast_state + "地瓜"

# # 创建地瓜对象
# sweet_potato = SweetPotato()
# print("-----------地瓜准备好了，可以开始烤啦-----------------------")
# print(sweet_potato)
# print("-----------接下来先烤4分钟---------------------------------")
# sweet_potato.roast(4)
# print(sweet_potato)
# print("-----------接下来再继续烤3分钟---------------------------------")
# sweet_potato.roast(3)
# print(sweet_potato)
# print("-----------接下来添加佐料---------------------------------")
# sweet_potato.add_condiment("老干妈")
# sweet_potato.add_condiment("番茄酱")
# print(sweet_potato)
# 创建烤地瓜的人
person = Person()
# 创建地瓜对象
sweet_potato = SweetPotato()
print("-----------地瓜准备好了，可以开始烤啦-----------------------")
person.show_info(sweet_potato)
print("-----------接下来先烤4分钟---------------------------------")
person.roast(sweet_potato, 4)
person.show_info(sweet_potato)
print("-----------接下来再继续烤3分钟---------------------------------")
person.roast(sweet_potato, 3)
person.show_info(sweet_potato)
print("-----------接下来添加佐料---------------------------------")
# 添加佐料也可以放到人类里面
sweet_potato.add_condiment("老干妈")
sweet_potato.add_condiment("番茄酱")
person.show_info(sweet_potato)



# 房子类
class Home(object):
    # 提供构造方法，给对象添加属性及初始化
    def __init__(self, area):
        # 房子的可用面积
        self.area = area
        # 家具列表
        self.furniture_list = []


    # 添加家具
    def add_furniture(self, furniture):
        if self.area > furniture.area:
            # 放入到家具列表
            self.furniture_list.append(furniture)
            # 修改房子的可用面积
            self.area -= furniture.area
            print("ok，家具放入成功")
        else:
            print("对不起， 房子的可用面积为:%d 家具的面积为:%d" % (self.area, furniture.area))

    # 显示房子的描述信息
    def __str__(self):
        if self.furniture_list:
            # 显示家具信息
            # ”房子的可用面积为: 126 家具有: 喜临门, 长虹“
            # print(self.furniture_list)
            # 1. 遍历家具列表，完成获取家具名称，然后把家具名称放入到新的列表里面
            print(self.furniture_list)
            furniture_name_list = []
            for furniture in self.furniture_list:
                furniture_name_list.append(furniture.name)
            # # 2. 列表推导式
            # furniture_name_list = [furniture.name for furniture in self.furniture_list]

            return "房子的可用面积为:%d" % self.area + " 家具有:" + ",".join(furniture_name_list)
        else:
            return "房子的可用面积为:%d" % self.area


# 家具类
class Furniture(object):
    def __init__(self, name, area):
        # 家具名称
        self.name = name
        # 家具的面积
        self.area = area

    # 显示家具的描述信息
    def __str__(self):
        return "家具的名字:%s 面积:%d" % (self.name, self.area)



# 创建对象
home = Home(130)
print(home)

bed = Furniture("喜临门", 4)
print(bed)

# 添加家具
home.add_furniture(bed)

tv = Furniture("长虹", 4)
print(tv)
home.add_furniture(tv)


print(home)

