# 定义一个函数
def show_num():
    num = 10
    print(num)

show_num()

def show_num(num):
    print(num)

show_num(20)
# 调用第一个函数,在python里面函数如果相同,后面会把之前定义的函数覆盖,
# 以前的函数不能在最后使用,
# 如果没有特殊的需求,函数不要相同
