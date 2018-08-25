import re
if __name__ == '__main__':
    str_one = 'chuanzhi2345'
    str_two = 'a b;fsdfds,Abc Bca'
    pattern = re.compile('\d+')

    #1. 替换sub,把str_one里面的匹配到的数字替换成空得到chuanzhi
    result = pattern.sub("", str_one)
    #分组之后还可以调换位置(根据需求使用)
    pattern2 = re.compile(('(\w+) (\w+)'))
    result = pattern2.sub(r'\2 \1', str_two)

    #2.匹配中文unicode字符集才能匹配中文
    chinese_str = '小明和老王是邻居 no'
    chi_pattern = re.compile('[\u4e00-\u9fa5]+')
    result = chi_pattern.findall(chinese_str)
    #3.split分割


    print(result)
