import json
"""
1. JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，
    它使得人们很容易的进行阅读和编写。同时也方便了机器进行解析和生成。
    适用于进行数据交互的场景，比如网站前台与后台之间的数据交互。
2. json简单说就是javascript中的对象和数组，所以这两种结构就是对象和数组两种结构，
    通过这两种结构可以表示各种复杂的结构

    对象：对象在js中表示为{ }括起来的内容，数据结构为 { key：value, key：value, ... }
    的键值对的结构，在面向对象的语言中，key为对象的属性，value为对应的属性值，
    所以很容易理解，取值方法为 对象.key 获取属性值，这个属性值的类型可以是数字、字符串、数组、对象这几种。

    数组：数组在js中是中括号[ ]括起来的内容，数据结构为 ["Python", "javascript", "C++", ...]，
    取值方式和所有语言中一样，使用索引获取，字段值的类型可以是 数字、字符串、数组、对象几种。



    -------------
                - ---------json.loads()---------------------->
    json字符串   -
                -                                        python数据类型
                -
                - <---------json.dumps()----------------------
    -------------





    -------------
    包含json的类 ------------json.load()------------------------->
    文件对象     -
                -                                           python数据类型
                -
                - <---------json.dump()-------------------------
                -
    -------------
     具有read()或者write()方法的对象就是类文件对象，比如f = open(“a.txt”,”r”) f就是类文件对象
"""
#demo:
if __name__ == '__main__':
    json_str = '{"name":"雷不死","age":53}'
    # 1.将json字符串 转换成  py的字典 dict list
    dict_python = json.loads(json_str)
    print(type(dict_python))

    # 2. 把 py字典,list 转成 json字符串
    json_dict = {"name": "雷不死", "age": 53}
    str_json = json.dumps(json_dict)
    print(type(str_json))

    # 3.文件对象
    # 3.1 读取文件json数据, 转换成 py类型dict list
    fp = open('01data.json', 'r')
    print(type(fp))
    fp_dict_data = json.load(fp)

    # 3.2 将list dict 写入文件
    fp_write = open('01data2.json', 'w')
    json.dump(json_dict, fp_write)

    print(type(fp_dict_data))
    print(fp_dict_data)





































