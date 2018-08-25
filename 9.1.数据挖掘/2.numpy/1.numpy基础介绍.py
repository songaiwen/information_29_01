"""
1.numpy的介绍
    Numpy（Numerical Python）是一个开源的Python科学计算库，用于快速处理任意维度的数组。

    Numpy支持常见的数组和矩阵操作。对于同样的数值计算任务，使用Numpy比直接使用Python要简洁的多。

    Numpy使用ndarray对象来处理多维数组，该对象是一个快速而灵活的大数据容器。

2.ndarray介绍
    NumPy提供了一个N维数组类型ndarray，它描述了相同类型的“items”的集合。
    核心对象就是ndarry

3.ndarray与Python原生list运算效率对比
    import random
    import time
    import numpy as np
    a = []
    for i in range(1000000):
        a.append(random.random())
    t1 = time.time()
    sum1=sum(a)
    t2=time.time()

    b=np.array(a)
    t4=time.time()
    sum3=np.sum(b)
    t5=time.time()
    print(t2-t1, t5-t4)
    #t2-t1为使用python自带的求和函数消耗的时间，t5-t4为使用numpy求和消耗的时间，结果为：
    0.038883209228515625 0.0030972957611083984
    从中我们看到ndarray的计算速度要快很多，节约了时间。

    机器学习的最大特点就是大量的数据运算
    Numpy专门针对ndarray的操作和运算进行了设计，所以数组的存储效率和输入输出性能远优于Python中的嵌套列表，数组越大，Numpy的优势就越明显。

4.ndarray 的优势
    1.内存块风格
        ndarray在存储数据的时候，数据与数据的地址都是连续的，这样就给使得批量操作数组元素时速度更快。
        这是因为ndarray中的所有元素的类型都是相同的，而Python列表中的元素类型是任意的，
        所以ndarray在存储元素时内存可以连续，而python原生lis就t只能通过寻址方式找到下一个元素，
        这虽然也导致了在通用性能方面Numpy的ndarray不及Python原生list，但在科学计算中，
        Numpy的ndarray就可以省掉很多循环语句，代码使用方面比Python原生list简单的多。

    2. ndarray支持并行化运算（向量化运算）
    3 Numpy底层使用C语言编写，内部解除了GIL（全局解释器锁），其对数组的操作速度不受Python解释器的限制，效率远高于纯Python代码。

5.ndarray的属性
    属性名字	                    属性解释
    ndarray.shape	        数组维度的元组
    ndarray.ndim	        数组维数
    ndarray.size	        数组中的元素数量
    ndarray.itemsize	    一个数组元素的长度（字节）
    ndarray.dtype	        数组元素的类型

6. ndarray的类型   dtype是numpy.dtype类型，先看看对于数组来说都有哪些类型

    名称	                描述	                                    简写
    np.bool	        用一个字节存储的布尔类型（True或False）	        'b'
    np.int8	        一个字节大小，-128 至 127	                    'i'
    np.int16	    整数，-32768 至 32767	                        'i2'
    np.int32	        整数，-2 31 至 2 32 -1	                'i4'
    np.int64	    整数，-2 63 至 2 63 - 1	                    'i8'
    np.uint8	        无符号整数，0 至 255	                     'u'
    np.uint16	    无符号整数，0 至 65535	                    'u2'
    np.uint32	    无符号整数，0 至 2 ** 32 - 1	                'u4'
    np.uint64	    无符号整数，0 至 2 ** 64 - 1	                'u8'
    np.float16	    半精度浮点数：16位，正负号1位，指数5位，精度10位	'f2'
    np.float32	    单精度浮点数：32位，正负号1位，指数8位，精度23位	'f4'
    np.float64	    双精度浮点数：64位，正负号1位，指数11位，精度52位	'f8'
    np.complex64	复数，分别用两个32位浮点数表示实部和虚部	        'c8'
    np.complex128	复数，分别用两个64位浮点数表示实部和虚部	        'c16'
    np.object_	    python对象	                                 'O'
    np.string_	    字符串	'S'
    np.unicode_	    unicode类型	                                'U'

    创建数组的时候指定类型
    a = np.array([1,2,4], dtype=float)
    注意：若不指定，整数默认int64，小数默认float64


"""