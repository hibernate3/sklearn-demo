import random
import matplotlib.pyplot as plt
from pylab import mpl


def func1():
    '''
    实现基础绘制折线图
    :return:
    '''

    # 设置显示中文字体
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    # 设置正常显示符号
    mpl.rcParams['axes.unicode_minus'] = False

    # 准备x，y坐标的数据
    x = range(60)
    y_shanghai = [random.uniform(15, 18) for i in x]
    y_beijing = [random.uniform(1, 3) for i in x]

    # 创建画布
    plt.figure(figsize=(20, 8), dpi=80)

    # 绘制折线图
    plt.plot(x, y_shanghai, label='上海')
    plt.plot(x, y_beijing, color='r', linestyle='--', label='北京')

    # 添加x，y轴刻度
    x_ticks_label = ['11点{}分'.format(i) for i in x]
    y_ticks = range(40)

    # 修改x，y轴坐标刻度显示
    plt.xticks(x[::5], x_ticks_label[::5])
    plt.yticks(y_ticks[::5])

    # 添加描述信息
    plt.xlabel('时间')
    plt.ylabel('温度')
    plt.title('中午11点0分到12点之间的温度变化图示', fontsize=20)

    # 添加网格显示
    plt.grid(True, linestyle='--', alpha=0.5)

    plt.legend(loc='best')

    # 图像保存
    plt.savefig('test.png')

    # 显示图像
    plt.show()

    return None


def func2():
    '''
    多坐标绘图
    :return:
    '''
    # 设置显示中文字体
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    # 设置正常显示符号
    mpl.rcParams['axes.unicode_minus'] = False

    # 准备数据
    x = range(60)
    y_shanghai = [random.uniform(15, 18) for i in x]
    y_beijing = [random.uniform(1, 5) for i in x]

    # 创建画布
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8), dpi=100)

    # 绘制图像
    axes[0].plot(x, y_shanghai, label='上海')
    axes[1].plot(x, y_beijing, color='r', linestyle='--', label='北京')

    # 构造x，y轴刻度标签
    x_ticks_label = ['11点{}分'.format(i) for i in x]
    y_ticks = range(40)

    # 刻度显示
    axes[0].set_xticks(x[::5])
    axes[0].set_yticks(y_ticks[::5])
    axes[0].set_xticklabels(x_ticks_label[::5])

    axes[1].set_xticks(x[::5])
    axes[1].set_yticks(y_ticks[::5])
    axes[1].set_xticklabels(x_ticks_label[::5])

    # 添加网格显示
    axes[0].grid(True, linestyle="--", alpha=0.5)
    axes[1].grid(True, linestyle="--", alpha=0.5)

    # 添加描述信息
    axes[0].set_xlabel("时间")
    axes[0].set_ylabel("温度")
    axes[0].set_title("中午11点--12点某城市温度变化图", fontsize=20)
    axes[1].set_xlabel("时间")
    axes[1].set_ylabel("温度")
    axes[1].set_title("中午11点--12点某城市温度变化图", fontsize=20)

    # 图像保存
    plt.savefig("test.png")

    # 添加图例
    axes[0].legend(loc=0)
    axes[1].legend(loc=0)

    # 图像显示
    plt.show()

    return None


def func3():
    '''
    散点图绘制
    :return:
    '''
    # 设置显示中文字体
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    # 设置正常显示符号
    mpl.rcParams['axes.unicode_minus'] = False

    # 准备数据
    x = [225.98, 247.07, 253.14, 457.85, 241.58, 301.01, 20.67, 288.64,
         163.56, 120.06, 207.83, 342.75, 147.9, 53.06, 224.72, 29.51,
         21.61, 483.21, 245.25, 399.25, 343.35]
    y = [196.63, 203.88, 210.75, 372.74, 202.41, 247.61, 24.9, 239.34,
         140.32, 104.15, 176.84, 288.23, 128.79, 49.64, 191.74, 33.1,
         30.74, 400.02, 205.35, 330.64, 283.45]
    # 创建画布
    plt.figure(figsize=(20, 8), dpi=100)
    # 2.绘制散点图
    plt.scatter(x, y)
    # 3.显示图像
    plt.show()

    return None


def func4():
    '''
    柱状图绘制
    :return:
    '''
    # 设置显示中文字体
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    # 设置正常显示符号
    mpl.rcParams['axes.unicode_minus'] = False

    # 准备数据
    # 电影名字
    movie_name = ['雷神3：诸神黄昏', '正义联盟', '东方快车谋杀案', '寻梦环游记', '全球风暴', '降魔传', '追捕', '七十七天', '密战', '狂兽', '其它']

    # 横坐标
    x = range(len(movie_name))

    # 票房数据
    y = [73853, 57767, 22354, 15969, 14839, 8725, 8716, 8318, 7916, 6764, 52222]

    # 创建画布
    plt.figure(figsize=(20, 8), dpi=100)

    # 绘制柱状图
    plt.bar(x, y, width=0.5, color=['b', 'r', 'g', 'y', 'c', 'm', 'y', 'k', 'c', 'g', 'b'])

    # 修改x轴的刻度显示
    plt.xticks(x, movie_name)

    # 添加网格显示
    plt.grid(linestyle="--", alpha=0.5)

    # 添加标题
    plt.title("电影票房收入对比")

    # 显示图像
    plt.show()

    return None


if __name__ == '__main__':
    # func1()
    # func2()
    # func3()
    func4()
    pass

