"""
1.生成0和1的数组

    empty(shape[, dtype, order]) empty_like(a[, dtype, order, subok])
    eye(N[, M, k, dtype, order])
    identity(n[, dtype])
    ones(shape[, dtype, order])
    ones_like(a[, dtype, order, subok])
    zeros(shape[, dtype, order]) zeros_like(a[, dtype, order, subok])
    full(shape, fill_value[, dtype, order])
    full_like(a, fill_value[, dtype, order, subok])

    demo:
    np.zeros([4,5])  生成一个4行5列的数组
    np.ones([3,4])   生成一个3行4列的数组

2.从现有数组生成
    array(object[, dtype, copy, order, subok, ndmin])
    asarray(a[, dtype, order])
    asanyarray(a[, dtype, order]) ascontiguousarray(a[, dtype])
    asmatrix(data[, dtype])
    copy(a[, order])

    demo:
    score = np.array(score)
    s1 = np.asarray(score)
    s2 = np.copy(score)
    当我们改变score里面的数值的时候
    score[0] = 100
    score和s1的值都会变化 相当于浅拷贝
    s2的值是不会变化的,相当于深拷贝

3.生成固定范围的数组
    np.linspace (start, stop, num, endpoint, retstep, dtype)
    生成等间隔的序列

    start 序列的起始值
    stop 序列的终止值，
    如果endpoint为true，该值包含于序列中
    num 要生成的等间隔样例数量，默认为50
    endpoint 序列中是否包含stop值，默认为ture
    retstep 如果为true，返回样例，
    以及连续数字之间的步长
    dtype 输出ndarray的数据类型

    demo:
    # 生成等间隔的数组
    np.linspace(0, 100, 10)


"""