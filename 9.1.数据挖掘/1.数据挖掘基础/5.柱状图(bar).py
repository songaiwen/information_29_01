"""
一.柱状图绘制(bar)
    1.需求1-对比每部电影的票房收入
        #准备数据电影名字
        movie_name = ['雷神3：诸神黄昏','正义联盟','东方快车谋杀案','寻梦环游记','全球风暴','降魔传','追捕','七十七天','密战','狂兽','其它']
        # 横坐标,
        x = range(len(movie_name))
        #票房数据
        y = [73853,57767,22354,15969,14839,8725,8716,8318,7916,6764,52222]
        #创建画布, 宽度变小,名字会重叠,需要设置名字旋转
        plt.figure(figsize=(10, 8), dpi=100)
        #绘制柱状图
        plt.bar(x, y, width=0.5, color=['b','r','g','y','c','m','y','k','c','g','b'])
        #修改x轴的刻度显示, rotation是设置文字旋转的.防止重叠显示
        plt.xticks(x, movie_name, rotation=45)
        #添加网格显示
        plt.grid(True, linestyle="--", alpha=0.5)
        #添加标题
        plt.title("电影票房收入对比")
        #显示图像
        plt.show()
    2.需求2-如何对比电影票房收入才更能加有说服力？
        比较相同天数的票房

        movie_name = ['雷神3：诸神黄昏','正义联盟','寻梦环游记']
        first_day = [10587.6,10062.5,1275.7]
        first_weekend=[36224.9,34479.6,11830]
        x = range(len(movie_name))
        #创建画布对象
        plt.figure(figsize=(20,8), dpi=100)
        plt.bar(x, first_day,width=0.2)
        plt.bar([i+0.2 for i in x], first_weekend, width=0.2)
        #设置刻度显示信息
        plt.xticks([i+0.1 for i in x], movie_name)
        plt.show()
"""