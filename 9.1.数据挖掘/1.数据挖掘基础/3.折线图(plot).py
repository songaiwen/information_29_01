"""
1.matplotlib.pyplot模块
    matplotlib.pytplot包含了一系列类似于matlab的画图函数。 它的函数作用于当前图形(figure)的当前坐标系(axes)。
    import matplotlib.pyplot as plt

2.折线图绘制与显示,设置画布属性和图片保存(plot)
    # 创建画布对象
    #figure是创建画布的方法,如果不传参数,会显示默认大小
    #figsize是画布的大小,传的元组,
    #dpi是像素密度,显示画布的清晰度,密度越高显示越清晰
    plt.figure(figsize=(20, 8), dpi=100)
    x = [1,2,3,4,5,6,7]
    y = [17,17,18,15,11,11,13]
    # 绘制折线图
    plt.plot(x, y)
    #将画布保存为图像
    plt.savefig("test.png")
    # 显示折线图
    plt.show()

3.完善原始折线图1(辅助显示层)
    import random
    #1.准备x,y坐标的数据
    x = range(61)
    y = [random.uniform(15, 19) for _ in x]

    #6.设置北京的温度
    y_beijing = [random.uniform(2,5) for _ in x]
    #1.创建画布
    plt.figure(figsize=(20, 8), dpi=100)

    #2.绘制图形
    plt.plot(x, y, label="上海")

    #7.显示北京温度的变化,  linestyle两个横线表示虚线 ,一个横线后面一个点表示点划线
    #color是设置线的颜色
    plt.plot(x, y_beijing, linestyle="--", color="r", label="北京")

    #10.设置图例说明显示的位置,不传参数,使用默认值,会选择一个最优的位置显示,
    #可以根据需要
    plt.legend()

    #4.设置辅助显示层,刻度信息
    #yticks有两个参数,第一个是刻度值,第二个是刻度描述信息
    #先确定yticks的整体范围值
    y_ticks = range(41)
    #可以设置步长来控制显示刻度的范围
    plt.yticks(y_ticks[::5])

    #5.设置刻度描述信息
    x_ticks = ["11点{}分".format(i) for i in x]
    plt.xticks(x[::5], x_ticks[::5])

    #8.设置标题
    plt.title("11点到12点1小时内每分钟的温度变化折线图")
    plt.xlabel("时间")
    plt.ylabel("温度")

    #9.添加网格显示
    plt.grid(True, linestyle="--", color="r", alpha=0.6)

    #3.显示图像
    plt.show()

4.多个坐标系显示plt.subplots,面向对象的画图方法
    注意：plt.函数名()相当于面向过程的画图方法，axes.set_方法名()相当于面向对象的画图方法。

    import random
    #准备x,y坐标的数据
    x = range(61)
    y = [random.uniform(15, 19) for _ in x]

    #6.设置北京的温度
    y_beijing = [random.uniform(2,5) for _ in x]
    #1.创建画布
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20,8), dpi=100)
    axes[0].plot(x, y, label="上海")
    axes[1].plot(x, y_beijing, linestyle="--", color="r", label="北京")

    axes[0].legend()
    axes[1].legend()

    #先确定yticks的整体范围值
    y_ticks = range(41)
    #可以设置步长来控制显示刻度的范围
    axes[0].set_yticks(y_ticks[::5])
    axes[1].set_yticks(y_ticks[::5])

    #5.设置刻度描述信息
    x_ticks = ["11点{}分".format(i) for i in x]
    #axes无法设置刻度描述信息
    axes[0].set_xticks(x[::5], x_ticks[::5])
    axes[1].set_xticks(x[::5], x_ticks[::5])

    #8.设置标题
    axes[0].set_title("上海11点到12点1小时内每分钟的温度变化折线图")
    axes[1].set_title("北京11点到12点1小时内每分钟的温度变化折线图")
    axes[0].set_xlabel("时间")
    axes[1].set_ylabel("温度")
    axes[0].set_xlabel("时间")
    axes[1].set_ylabel("温度")
    #9.添加网格显示
    axes[0].grid(True, linestyle="--", color="r", alpha=0.6)
    axes[1].grid(True, linestyle="--", color="r", alpha=0.6)

    #3.显示图像
    plt.show()

5.设置图形的风格
    颜色字符	        风格字符
    r 红色	        - 实线
    g 绿色	        - - 虚线
    b 蓝色	        -. 点划线
    w 白色	        : 点虚线
    c 青色	        ' ' 留空、空格
    m 洋红
    y 黄色
    k 黑色

6.折线图的应用场景
    呈现公司产品(不同区域)每天活跃用户数

    呈现app每天下载数量

    呈现产品新功能上线后,用户点击次数随时间的变化

    拓展：画各种数学函数图像
    import numpy as np
    x = np.linspace(-10, 10, 100000)
    y = x * x * x
    plt.figure(figsize=(20, 8), dpi=80)
    plt.plot(x, y)
    plt.show()

"""