import time

def timeit(func):

    def wrapper():
        start = time.clock()
        func()
        stop = time.clock()
        result = stop - start
        print(stop)
        return wrapper

@timeit
def foo():
    print("函数的执行时间是:")

foo()