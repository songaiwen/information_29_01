"""
1.饼图介绍
    饼图广泛得应用在各个领域，用于表示不同分类的占比情况，通过弧度大小来对比各种分类。
    饼图通过将一个圆饼按照分类的占比划分成多个区块，整个圆饼代表数据的总量，
    每个区块（圆弧）表示该分类占总体的比例大小，所有区块（圆弧）的加和等于 100%。

2.饼图绘制

#1.准备数据
movie_name = ['雷神3：诸神黄昏','正义联盟','东方快车谋杀案','寻梦环游记','全球风暴','降魔传','追捕','七十七天','密战','狂兽','其它']

place_count = [60605,54546,45819,28243,13270,9945,7679,6799,6101,4621,20105]
#2.创建画布
plt.figure(figsize=(20, 8), dpi=100)
#3.绘制饼图
    '''
    注意显示的百分比的位数
    plt.pie(x, labels=,autopct=,colors)
        x:数量，自动算百分比
        labels:每部分名称
        autopct:占比显示指定%1.2f%%
        colors:每部分颜色
    '''
plt.pie(place_count, labels=movie_name, autopct="%1.2f%%", colors=['b','r','g','y','c','m','y','k','c','g','y'])
#4.显示图例
plt.legend()
#5.添加标题
plt.title("电影排片占比")
#7.为了让显示的饼图保持圆形，需要添加axis保证长宽一样
plt.axis("equal")
#6.显示图像
plt.show()



3. 添加阴影部分,增加破裂效果
import matplotlib.pyplot as plt
# 1）准备参数
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)

# 2）创建绘图区
fig1, ax1 = plt.subplots()

# 3）绘制饼图
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)

# 4）显示正圆
ax1.axis('equal')

# 5）显示图像
plt.show()


"""