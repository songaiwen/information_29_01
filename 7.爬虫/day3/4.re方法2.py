"""
正则表达式:

"""
import re

if __name__ == '__main__':

    str_one = 'abc123'
    str_two = '456'
    pattern = re.compile('^\d+$')

    # 1.match 从头开始 匹配一次
    result = pattern.match(str_one)
    print(result)

    # 2.search 从任意位置
    result = pattern.search(str_one)
    print(result)

    #3.findall 返回list
    str_two = 'afdsdafsfsdfsdsdsd'
    pattern = re.compile('s')
    result = pattern.findall(str_two)


    #4.finditer  返回iter
    result = pattern.finditer(str_two)
    # for res in result:


    print(result)