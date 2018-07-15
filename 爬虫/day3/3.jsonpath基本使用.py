
"""
用来解析多层嵌套的json数据;JsonPath 是一种信息抽取类库，是从JSON文档中抽取指定信息的工具，提供多种语言实现版本，包括：Javascript, Python， PHP 和 Java。
JsonPath 对于 JSON 来说，相当于 XPath 对于 XML。

XPath	JSONPath	描述
/	        $	    根节点
.	        @	    现行节点
/	        .or[]	取子节点
..	        n/a	    取父节点，Jsonpath未支持
//	        ..	    就是不管位置，选择所有符合条件的条件
*	        *	    匹配所有元素节点
@	        n/a	    根据属性访问，Json不支持，因为Json是个Key-value递归结构，不需要属性访问。
[]	        []	    迭代器标示（可以在里边做简单的迭代操作，如数组下标，根据内容选值等）
|	        [,]	    支持迭代器中做多选。
[]	        ?()	    支持过滤操作.
n/a	        ()	    支持表达式计算
()	        n/a	    分组，JsonPath不支持

"""
import json, jsonpath, requests

def load_lagou_data():
    #目标url
    url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
    #设置请求头
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    #发送请求请求数据
    response = requests.get(url, headers=headers)
    #默认的字符集是utf-8
    data = response.content.decode()
    print(data)

    # 此写法 只有在 网址尾缀为 /abc.json的时候使用 返回的是Python 的字典或者list
    # data = response.json()

    #1.将data转换成pythondict或者list(因为默认的是字符串)
    dict_data_python = json.loads(data)
    print(dict_data_python)

    #2.使用jsonpath解析出所有的城市名字,返回的是list数据类型,所以取数据的时候需要遍历
    city_list = jsonpath.jsonpath(dict_data_python, '$..name')
    # city_list = jsonpath.jsonpath(dict_data_python, '$..A..name')
    for i in city_list:
        print(i)
    print(city_list)

if __name__ == '__main__':
    load_lagou_data()